import json, os, re, sys, time, hashlib, subprocess, glob, shutil
REL = 'audio-fa'
VOICE = 'fa_IR-amir-medium'
ONLY = os.environ.get('ONLY', '').strip()
BUDGET = float(os.environ.get('BUDGET_MIN', '320')) * 60
DRY = os.environ.get('DRY') == '1'
T0 = time.time()
OUT = 'audio_out'
os.makedirs(OUT, exist_ok=True)

def sh(cmd, **kw):
    return subprocess.run(cmd, **kw)

if not DRY:
    if sh(['gh', 'release', 'view', REL], capture_output=True).returncode != 0:
        sh(['gh', 'release', 'create', REL, '-t', 'Persian audio', '-n', 'Generated Persian lesson audio'], check=True)
    sh(['gh', 'release', 'download', REL, '-p', 'hashes.json', '-D', OUT, '--clobber'], capture_output=True)

hp = os.path.join(OUT, 'hashes.json')
hashes = json.load(open(hp)) if os.path.exists(hp) else {}

def clean(t):
    t = t.replace('**', '').replace('#', '')
    t = re.sub(r'[`$_>]', '', t)
    t = t.replace('|', ' ')
    t = re.sub(r'\n{2,}', '\n', t)
    return t.strip()

idx = json.load(open('index.json', encoding='utf8'))
lessons = []
def walk(x):
    if isinstance(x, dict):
        if x.get('country') == 'IR' and 'chapters' in x:
            for c in x['chapters']:
                for l in c.get('lessons', []):
                    lessons.append((c['id'], l['id'], l['title']))
        for v in x.values(): walk(v)
    elif isinstance(x, list):
        for v in x: walk(v)
walk(idx)

jobs = []
for cid, lid, title in lessons:
    if ONLY and lid != ONLY: continue
    p = f'details/{lid}.md'
    if os.path.exists(p):
        jobs.append((f'{lid}-d', clean(open(p, encoding='utf8').read())))
    sp = f'summaries/{cid}.json'
    if os.path.exists(sp):
        s = json.load(open(sp, encoding='utf8')).get(title)
        if s: jobs.append((f'{lid}-s', clean(s)))
print('lessons', len(lessons), 'jobs', len(jobs))

pending = []
def upload():
    global pending
    if not pending or DRY: pending = []; return
    json.dump(hashes, open(hp, 'w'))
    sh(['gh', 'release', 'upload', REL, hp] + pending + ['--clobber'], check=True)
    for f in pending:
        if f.endswith('.mp3'): os.remove(f)
    pending = []

done = 0
for name, text in jobs:
    if time.time() - T0 > BUDGET:
        print('time budget reached, rerun to continue'); break
    if not text: continue
    h = hashlib.sha1(text.encode('utf8')).hexdigest()
    if hashes.get(name) == h: continue
    wav = os.path.join(OUT, name + '.wav')
    mp3 = os.path.join(OUT, name + '.mp3')
    if DRY:
        print('would make', name, len(text)); done += 1; continue
    sh(['python3', '-m', 'piper', '-m', VOICE, '-f', wav], input=text.encode('utf8'), check=True)
    sh(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-ac', '1', '-b:a', '32k', mp3], check=True)
    os.remove(wav)
    hashes[name] = h
    pending.append(mp3)
    done += 1
    print('made', name, flush=True)
    if len(pending) >= 20: upload()
upload()
print('done', done)
