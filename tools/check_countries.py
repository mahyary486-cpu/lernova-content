#!/usr/bin/env python3
"""Pre-push safety check for the shared Lernova content repo.

Several people / Claude accounts add countries to this repo at the same time. This script makes sure
your commit does not remove anyone else's work. Run it right before `git push`:

    git pull --rebase && python3 tools/check_countries.py && git push origin main

It compares your working tree with origin/main and FAILS if
  1. a country, chapter or lesson that exists on origin/main is missing from your index.json,
  2. any file that exists on origin/main is deleted,
  3. you changed manifest.json or anything in packs/ (the GitHub Action builds those; never commit them).
"""
import json, subprocess, sys

def git(*a):
    r = subprocess.run(['git'] + list(a), capture_output=True, text=True)
    return r.returncode, r.stdout

def tree_ids(index):
    out = set()
    for g in index.get('grades', []):
        cc = g.get('country', 'US')
        out.add((cc,))
        for c in g.get('chapters', []):
            out.add((cc, c['id']))
            for l in c.get('lessons', []):
                out.add((cc, c['id'], l['id']))
    return out

ok = True
def say(good, msg):
    global ok
    ok = ok and good
    print(('✅ ' if good else '❌ ') + msg)

subprocess.run(['git', 'fetch', '-q'])
rc, _ = git('rev-parse', '--verify', '-q', 'origin/main')
base = 'origin/main' if rc == 0 else 'HEAD'
rc, remote_index = git('show', base + ':index.json')
mine = json.load(open('index.json', encoding='utf-8'))
theirs = json.loads(remote_index) if rc == 0 and remote_index.strip() else {'grades': []}
lost = sorted(tree_ids(theirs) - tree_ids(mine))
countries_lost = sorted({t[0] for t in lost if len(t) == 1})
say(not lost, 'index.json keeps every country, chapter and lesson that is on %s' % base +
    ('' if not lost else '  -> MISSING: countries %s, plus %d chapters/lessons (first: %s)' % (
        countries_lost or 'none', len(lost), lost[:3])))

# committed + uncommitted changes versus the remote
rc, diff = git('diff', '--name-status', base)
changes = [l.split('\t') for l in diff.strip().split('\n') if l.strip()]
deleted = [c[-1] for c in changes if c[0].startswith('D')]
say(not deleted, 'no file from %s is deleted' % base + ('' if not deleted else '  -> DELETED: %s' % deleted[:5]))
generated = [c[-1] for c in changes if c[-1] == 'manifest.json' or c[-1].startswith('packs/')]
say(not generated, 'manifest.json and packs/ are untouched (the GitHub Action builds them)' +
    ('' if not generated else '  -> run: git checkout %s -- manifest.json packs' % base))
touched = sorted({c[-1].split('/')[0] for c in changes})
print('ℹ️ folders you changed:', ', '.join(touched) if touched else 'nothing')
print('\n🟢 safe to push' if ok else '\n🔴 do NOT push; fix the lines marked ❌ first')
sys.exit(0 if ok else 1)
