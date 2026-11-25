#!/usr/bin/env python3
"""Iran (IR) content progress report. Run from the repo root:  python3 tools/ir_progress.py
Counts what exists in index.json + details/ + summaries/ + banks/ and compares the
number of chapters with TARGET (a rough estimate of the official books: edit it freely)."""
import json, os, re

# subject key -> {grade: official chapter count (ESTIMATE, edit me)}
TARGET = {
    'Mathematics': {9: 8, 10: 7, 11: 5, 12: 5},
    'Science':     {9: 15},
    'Physics':     {10: 5, 11: 4, 12: 5},
    'Chemistry':   {10: 3, 11: 3, 12: 4},
}
FA = re.compile(r'[\u0600-\u06FF]')

def persian(path):
    if not os.path.exists(path):
        return False
    t = open(path, encoding='utf-8').read()
    letters = len(FA.findall(t))
    return letters > 0.3 * max(1, len(re.findall(r'\w', t)))

ix = json.load(open('index.json', encoding='utf-8'))
rows = []
tot = dict(t_ch=0, reg=0, lessons=0, fa=0, bank=0, ch_done=0)
for g in sorted((x for x in ix['grades'] if x.get('country') == 'IR'), key=lambda x: (x['grade'], x['subject'])):
    sub, gr = g['subject'], g['grade']
    chs = g['chapters']
    target = TARGET.get(sub, {}).get(gr, len(chs))
    n_les = sum(len(c['lessons']) for c in chs)
    n_fa = 0
    n_bank = 0
    n_done = 0
    for c in chs:
        les_fa = [persian('details/%s.md' % l['id']) for l in c['lessons']]
        n_fa += sum(les_fa)
        has_bank = os.path.exists('banks/%s.txt' % c['id'])
        n_bank += has_bank
        if all(les_fa) and les_fa and has_bank and os.path.exists('summaries/%s.json' % c['id']):
            n_done += 1
    rows.append((gr, sub, len(chs), target, n_les, n_fa, n_bank, n_done))
    tot['t_ch'] += target; tot['reg'] += len(chs); tot['lessons'] += n_les
    tot['fa'] += n_fa; tot['bank'] += n_bank; tot['ch_done'] += n_done

print('%-6s %-12s %9s %8s %11s %7s %8s' % ('grade', 'subject', 'chapters', 'lessons', 'FA lessons', 'banks', 'complete'))
for gr, sub, reg, target, nl, nf, nb, nd in rows:
    print('%-6s %-12s %4d/%-4d %8d %11d %5d/%-2d %8d' % (gr, sub, reg, target, nl, nf, nb, reg, nd))
print()
pct = lambda a, b: (100.0 * a / b) if b else 0.0
print('Chapters complete (lessons in Persian + summary + exam bank): %d of ~%d  = %.0f%%' % (tot['ch_done'], tot['t_ch'], pct(tot['ch_done'], tot['t_ch'])))
print('Chapters registered in the app:                               %d of ~%d  = %.0f%%' % (tot['reg'], tot['t_ch'], pct(tot['reg'], tot['t_ch'])))
print('Registered lessons written in Persian:                        %d of %d  = %.0f%%' % (tot['fa'], tot['lessons'], pct(tot['fa'], tot['lessons'])))
print('(The "~" targets are rough estimates of the official books; edit TARGET at the top.)')
