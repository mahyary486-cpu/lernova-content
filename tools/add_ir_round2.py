#!/usr/bin/env python3
"""Registers the Iran round-2 chapters in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_round2.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))

NEW = [
 (10, 'Mathematics', 'ir10m-ch4', 'Equations and Inequalities', [
   'Solving quadratic equations', 'The quadratic formula and the discriminant',
   'Rational and radical equations', 'Linear and quadratic inequalities']),
 (10, 'Physics', 'ir10p-ch1', 'Physics and Measurement', [
   'Physics and modeling', 'Measurement and units', 'Precision and scientific notation']),
 (10, 'Chemistry', 'ir10c-ch1', 'The Cosmos: Birthplace of the Elements', [
   'Origin of the elements', 'Atomic structure, isotopes and atomic mass',
   'Electron arrangement and the periodic table']),
]
for grade, subject, cid, title, lessons in NEW:
    g = next((x for x in ix['grades'] if x.get('country') == 'IR' and x['grade'] == grade and x['subject'] == subject), None)
    if g is None:
        g = {'grade': grade, 'subject': subject, 'country': 'IR', 'chapters': []}
        ix['grades'].append(g)
    if any(c['id'] == cid for c in g['chapters']):
        continue
    g['chapters'].append({'id': cid, 'title': title,
        'lessons': [{'id': '%s-l%d' % (cid, i + 1), 'title': t} for i, t in enumerate(lessons)]})
json.dump(ix, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('index.json updated (IR only)')
