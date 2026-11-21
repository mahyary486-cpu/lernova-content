#!/usr/bin/env python3
"""Registers Iran grade 11 math (Calculus 1, chapters 1-3) in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_g11m_r1.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))
NEW = [('ir11m-ch2', 'Calculus 1: Algebra and Equations', ['Arithmetic and Geometric Sequences and Their Sums', "Quadratic Equations, Discriminant and Vieta's Formulas", 'The Parabola: Vertex, Graph and Extreme Values', 'Sign Determination and Quadratic Inequalities', 'Rational and Radical Equations']), ('ir11m-ch3', 'Calculus 1: Functions', ['Function Concept, Domain and Range', 'Absolute Value, Floor and Piecewise Functions', 'Operations on Functions and Composition', 'One-to-One Functions and Inverse Functions', 'Transformations of Function Graphs']), ('ir11m-ch4', 'Calculus 1: Trigonometry', ['Radian Measure and the Trigonometric Circle', 'Trigonometric Identities and Related Angles', 'Graphs of Sine and Cosine', 'Sum, Difference and Double-Angle Formulas', 'Solving Trigonometric Equations'])]
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
