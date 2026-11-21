#!/usr/bin/env python3
"""Registers Iran grade 11 math (Calculus 1, chapters 4-6) in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_g11m_r2.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))
NEW = [('ir11m-ch5', 'Calculus 1: Exponential and Logarithmic Functions', ['Rational Exponents and Radicals', 'Exponential Functions and Their Graphs', 'Logarithm: Definition and Properties', 'Logarithmic Functions and Their Graphs', 'Exponential and Logarithmic Equations']), ('ir11m-ch6', 'Calculus 1: Limits and Continuity', ['The Concept of a Limit and One-Sided Limits', 'Limit Rules and Algebraic Techniques', 'Limits at Infinity and Infinite Limits', 'Horizontal and Vertical Asymptotes', 'Continuity of Functions']), ('ir11m-ch7', 'Calculus 1: The Derivative', ['Average and Instantaneous Rate of Change', 'Derivative at a Point and the Tangent Line', 'Derivative Rules for Polynomials', 'Product, Quotient and Chain Rules', 'Applications: Monotonicity, Extrema and Motion'])]
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
