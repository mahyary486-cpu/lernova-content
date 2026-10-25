#!/usr/bin/env python3
"""Inventory of the Iran content: per chapter, what exists and in which language.
Run from the repo root:  python3 tools/inventory_ir.py"""
import json, os, re
def lang(text):
    fa = len(re.findall(r'[\u0600-\u06FF]', text)); la = len(re.findall(r'[A-Za-z]', text))
    return '—' if fa + la < 20 else ('فارسی' if fa > la else 'EN')
def rd(p): return open(p, encoding='utf8').read() if os.path.exists(p) else None
ix = json.load(open('index.json', encoding='utf-8'))
tot = {'ch': 0, 'det_fa': 0, 'det': 0, 'sum_fa': 0, 'bank_fa': 0, 'bank': 0}
for g in ix['grades']:
    if g.get('country') != 'IR': continue
    print('\n== %s | پایه %s' % (g['subject'], g['grade']))
    for c in g['chapters']:
        cid = c['id']; L = c['lessons']; tot['ch'] += 1
        dets = [rd('details/%s.md' % l['id']) for l in L]
        d_n = sum(1 for d in dets if d); d_fa = sum(1 for d in dets if d and lang(d) == 'فارسی')
        s = rd('summaries/%s.json' % cid); b = rd('banks/%s.txt' % cid)
        nq = len([l for l in b.split('\n')[1:] if l.strip()]) if b else 0
        sl = lang(s) if s else 'ندارد'; bl = lang(b) if b else 'ندارد'
        tot['det'] += d_n; tot['det_fa'] += d_fa
        tot['sum_fa'] += sl == 'فارسی'; tot['bank'] += bool(b); tot['bank_fa'] += bl == 'فارسی'
        print('%-9s %-34s درس %d | متن کامل %d/%d (فارسی %d) | خلاصه %s | آزمون %s%s' % (
            cid, c['title'][:34], len(L), d_n, len(L), d_fa, sl, bl, (' (%d سؤال)' % nq) if b else ''))
print('\nجمع: %d فصل | متن کامل فارسی %d از %d | خلاصه‌ی فارسی %d | آزمون: %d فصل (فارسی %d)' % (
    tot['ch'], tot['det_fa'], tot['det'], tot['sum_fa'], tot['bank'], tot['bank_fa']))
