#!/usr/bin/env python3
"""Registers Iran round-5 chapters (grade 11 physics ch2-4, chemistry ch2-3). Touches ONLY IR entries.
Skips any chapter id that already exists. Run from the repo root:  python3 tools/add_ir_round5.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))
P_, C = 'Physics', 'Chemistry'
NEW = [
 (11, P_, 'ir11p-ch2', 'Electric Current and DC Circuits', ["Current, resistance and Ohm's law", 'Series and parallel circuits', 'Electric power, EMF and internal resistance']),
 (11, P_, 'ir11p-ch3', 'Magnetism', ['Magnetic field and its sources', 'Force on a moving charge and on a current-carrying wire', 'Magnetic materials']),
 (11, P_, 'ir11p-ch4', 'Electromagnetic Induction and Alternating Current', ["Magnetic flux and Faraday's law", "Lenz's law and motional emf", 'Alternating current and transformers']),
 (11, C, 'ir11c-ch2', 'In Pursuit of Healthy Food', ['Reaction rate', 'Factors affecting reaction rate', 'Enthalpy and heat of reaction', 'Energy in food']),
 (11, C, 'ir11c-ch3', 'Clothing, an Endless Need', ['Hydrocarbons: alkanes and alkenes', 'Polymers and polymerization', 'Fibers, plastics and recycling']),
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
