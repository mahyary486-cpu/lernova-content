#!/usr/bin/env python3
"""Registers Iran grade 11 math (Statistics and Probability) in index.json. Touches ONLY IR entries.
Run from the repo root:  python3 tools/add_ir_g11m_r4.py"""
import json
P = 'index.json'
ix = json.load(open(P, encoding='utf-8'))
NEW = [('ir11m-ch11', 'Statistics and Probability: Probability', ['Sample Space, Events and the Rules of Probability', 'Counting Outcomes: With and Without Replacement', 'Conditional Probability', 'Independent Events', "Total Probability and Bayes' Rule"]), ('ir11m-ch12', 'Statistics and Probability: Descriptive Statistics', ['Data Types and Frequency Tables', 'Measures of Center', 'Measures of Spread: Range, Variance and Standard Deviation', 'Quartiles, Box Plots and Outliers', 'Standard Score and Coefficient of Variation']), ('ir11m-ch13', 'Statistics and Probability: Inferential Statistics', ['Population, Sample and Sampling Methods', 'Sample Mean and Standard Error', 'The Normal Distribution and the Empirical Rule', 'Confidence Intervals', 'Margin of Error and Sample Size'])]
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
