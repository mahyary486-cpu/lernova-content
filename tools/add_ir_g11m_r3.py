#!/usr/bin/env python3
"""Registers Iran grade 11 math (Geometry 2) in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_g11m_r3.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))
NEW = [('ir11m-ch8', 'Geometry 2: Circle', ['Central and Inscribed Angles in a Circle', 'Tangent Lines and the Tangent-Chord Angle', 'Angles Formed by Chords and Secants', 'Power of a Point and Lengths in a Circle', 'Arc Length, Sector Area and Two Circles']), ('ir11m-ch9', 'Geometry 2: Geometric Transformations', ['Reflection and Translation', 'Rotation', 'Composition of Transformations and Symmetry', 'Homothety (Dilation)', 'Similarity and Its Applications']), ('ir11m-ch10', 'Geometry 2: Length Relations in a Triangle', ['The Law of Sines', 'The Law of Cosines', 'Area of a Triangle', 'Medians, Angle Bisectors and Special Triangles', 'Solving Triangles and Applications'])]
g = next((x for x in ix['grades'] if x.get('country') == 'IR' and x['grade'] == 11 and x['subject'] == 'Mathematics'), None)
if g is None:
    g = {'grade': 11, 'subject': 'Mathematics', 'country': 'IR', 'chapters': []}
    ix['grades'].append(g)
print('existing IR grade 11 math chapters:', [(c['id'], c['title']) for c in g['chapters']])
taken = {l['title'] for x in ix['grades'] if x.get('country') == 'IR' for c in x['chapters'] for l in c['lessons']}
for cid, title, lessons in NEW:
    if any(c['id'] == cid for c in g['chapters']):
        print('skip (exists):', cid); continue
    items = []
    for i, t in enumerate(lessons):
        if t in taken: t = t + ' (Grade 11)'
        items.append({'id': '%s-l%d' % (cid, i + 1), 'title': t})
    g['chapters'].append({'id': cid, 'title': title, 'lessons': items})
    print('added:', cid, title)
json.dump(ix, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('index.json updated (IR only)')
