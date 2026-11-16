#!/usr/bin/env python3
"""Registers Iran round-4 chapters (grade 10 remainder) in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_round4.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))
M, P_, C = 'Mathematics', 'Physics', 'Chemistry'
NEW = [
 (10, M, 'ir10m-ch6', 'Counting Without Enumeration', ['Counting principles', 'Permutations and factorials', 'Combinations']),
 (10, M, 'ir10m-ch7', 'Probability and Statistics', ['Sample space and events', 'Probability rules', 'Measures of center and spread']),
 (10, P_, 'ir10p-ch3', 'Work, Energy and Power', ['Work and kinetic energy', 'Potential energy and conservation of mechanical energy', 'Power and efficiency']),
 (10, P_, 'ir10p-ch4', 'Temperature and Heat', ['Temperature and thermometers', 'Heat and specific heat', 'Heat transfer and thermal expansion']),
 (10, P_, 'ir10p-ch5', 'Thermodynamics', ['The first law of thermodynamics', 'Heat engines and the second law']),
 (10, C, 'ir10c-ch3', 'Water, the Rhythm of Life', ['Water, the solvent of life', 'Solubility and its factors', 'Concentration of solutions', 'Electrolytes and ions in solution']),
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
