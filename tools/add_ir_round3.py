#!/usr/bin/env python3
"""Registers Iran round-3 chapters (grades 10-12) in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_round3.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))

M, P_, C = 'Mathematics', 'Physics', 'Chemistry'
NEW = [
 (10, M, 'ir10m-ch5', 'Functions', ['The concept of a function', 'Domain, range and graphs', 'Piecewise and absolute value functions']),
 (10, P_, 'ir10p-ch2', 'Physical Properties of Matter', ['States of matter and intermolecular forces', 'Pressure in fluids', "Buoyancy and Archimedes' principle"]),
 (10, C, 'ir10c-ch2', 'Gases in Our Lives', ['Atmosphere layers and air composition', 'Gas laws and molar volume', 'Greenhouse gases and air pollution']),
 (11, M, 'ir11m-ch1', 'Quadratic Functions', ['The parabola and its vertex', 'Maximum and minimum applications', 'Transformations of graphs']),
 (11, P_, 'ir11p-ch1', 'Electrostatics', ["Electric charge and Coulomb's law", 'The electric field', 'Electric potential and potential difference']),
 (11, C, 'ir11c-ch1', "Earth's Gifts: Elements and Redox", ['Periodic trends in the table', 'Oxidation-reduction reactions', 'Activity series and corrosion']),
 (12, M, 'ir12m-ch1', 'Limits and Derivatives', ['The concept of a limit', 'The derivative and the tangent slope', 'Differentiation rules']),
 (12, P_, 'ir12p-ch1', 'Motion on a Straight Line', ['Position, displacement and velocity', 'Motion with constant acceleration', 'Free fall']),
 (12, C, 'ir12c-ch1', 'Cleansing Agents and Acids', ['Soap', 'Non-soap detergents', 'Acids, bases and pH']),
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
