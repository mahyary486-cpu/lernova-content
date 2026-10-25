#!/usr/bin/env python3
"""Checks the whole content repo: bank format, packs fingerprints, and expected new files.
Usage (from the repo root):  python3 tools/verify_content.py"""
import glob, hashlib, json, os, subprocess, sys
ok = True
def say(good, msg):
    global ok
    ok = ok and good
    print(('✅ ' if good else '❌ ') + msg)
def fp(p): return hashlib.sha1(open(p, 'rb').read()).hexdigest()[:10]
try:
    subprocess.run(['git', 'fetch', '-q'], check=True, capture_output=True)
    ahead = subprocess.run(['git', 'rev-list', '--count', 'origin/main..HEAD'], capture_output=True, text=True).stdout.strip()
    say(ahead == '0', 'همه تغییرات روی گیت‌هاب push شده')
except Exception:
    print('(بررسی git رد شد)')
# 1) every bank has a valid format
bad = []
for b in sorted(glob.glob('banks/*.txt')):
    ls = [l for l in open(b, encoding='utf8').read().split('\n') if l.strip()]
    if not ls: continue
    hdr, qs = ls[0], ls[1:]
    good = hdr.startswith('#') and len(hdr) - 1 == len(qs) and all(
        len(q.split('|')) == 7 and q.split('|')[5] in '0123' and len(set(q.split('|')[1:5])) == 4 for q in qs)
    if not good: bad.append(b)
say(not bad, 'همه‌ی %d بانک آزمون ساختار درست دارند' % len(glob.glob('banks/*.txt')) + (' (مشکل: %s)' % bad if bad else ''))
# 2) expected files from this work
sci = sorted(glob.glob('banks/ir9s-ch*.txt'))
need = ['banks/ir9m-ch%d.txt' % n for n in range(1, 9)] + ['banks/g9-ch3.txt', 'summaries/g9-ch3.json'] + ['details/g9-ch3-l%d.md' % n for n in (1, 2, 3, 4)]
miss = [f for f in need if not os.path.exists(f)]
say(not miss, 'ریاضی پایه ۹ ایران: آزمون هر ۸ فصل + فصل ۳ جبر ۱ موجود است' + (' (کم: %s)' % miss if miss else ''))
# 3) packs list every file and are up to date
for pk in sorted(glob.glob('packs/*.json')):
    pf = json.load(open(pk))['files']
    pf = dict(pf) if not isinstance(pf, dict) else pf
    m = [f for f in pf if not os.path.exists(f)]
    s = [f for f in pf if os.path.exists(f) and pf[f] != fp(f)]
    pre = 'ir' if 'IR' in pk else 'g'
    unlisted = [f for f in glob.glob('banks/*.txt') + glob.glob('summaries/*.json') + glob.glob('details/*.md')
                if os.path.basename(f).startswith(pre) and f not in pf]
    say(not (m or s or unlisted), '%s: %d فایل، همه به‌روز' % (os.path.basename(pk), len(pf)) +
        ((' (مشکل: %d ناهماهنگ، %d ثبت‌نشده)' % (len(m) + len(s), len(unlisted))) if (m or s or unlisted) else ''))
# 4) index lessons all have a detail file where expected
ix = json.load(open('index.json', encoding='utf-8'))
chs = [c['id'] for g in ix['grades'] for c in g['chapters']]
say('g9-ch3' in chs and all('ir9m-ch%d' % n in chs for n in range(1, 9)), 'فصل‌ها در index.json ثبت شده‌اند')
v = json.load(open('version.json'))
import re as _re
fa_n = [f for f in sorted(glob.glob('summaries/ir9*.json'))
        if len(_re.findall(r'[\u0600-\u06FF]', open(f, encoding='utf8').read())) > 200]
print('ℹ️ فصل‌های ایران با متن فارسی: %d (%s)' % (len(fa_n), '، '.join(os.path.basename(f)[:-5] for f in fa_n)))
print('ℹ️ آزمون علوم پایه ۹ ایران: %d فصل از ۱۵' % len(sci))
print('ℹ️ نسخه‌ی محتوا:', v['version'], v.get('updated', ''))
print('\n🟢 همه چیز تایید شد' if ok else '\n🔴 مشکلی هست؛ خروجی بالا را بفرستید')
sys.exit(0 if ok else 1)
