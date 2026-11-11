#!/usr/bin/env python3
"""Adds Japan (JP) grade 9 Mathematics to index.json and bumps version.json.
Reads the CURRENT index.json, touches only the JP grade 9 Mathematics entry, keeps everything else.
Run from the repo root:  python3 tools/add_jp.py"""
import json, os, datetime
CHAPTERS = json.loads('[{"id": "jp9m-ch1", "title": "多項式", "lessons": [{"id": "jp9m-ch1-l1", "title": "単項式と多項式の乗法・除法"}, {"id": "jp9m-ch1-l2", "title": "乗法公式と式の展開"}, {"id": "jp9m-ch1-l3", "title": "因数分解と式の利用"}]}, {"id": "jp9m-ch2", "title": "平方根", "lessons": [{"id": "jp9m-ch2-l1", "title": "平方根の意味と大小"}, {"id": "jp9m-ch2-l2", "title": "根号を含む式の計算"}, {"id": "jp9m-ch2-l3", "title": "有理化と平方根の利用"}]}, {"id": "jp9m-ch3", "title": "2次方程式", "lessons": [{"id": "jp9m-ch3-l1", "title": "因数分解と平方根の考え方で解く"}, {"id": "jp9m-ch3-l2", "title": "解の公式"}, {"id": "jp9m-ch3-l3", "title": "2次方程式の利用"}]}, {"id": "jp9m-ch4", "title": "関数 y=ax²", "lessons": [{"id": "jp9m-ch4-l1", "title": "y=ax² の式とグラフ"}, {"id": "jp9m-ch4-l2", "title": "変化の割合と変域"}, {"id": "jp9m-ch4-l3", "title": "関数 y=ax² の利用"}]}, {"id": "jp9m-ch5", "title": "相似な図形", "lessons": [{"id": "jp9m-ch5-l1", "title": "相似の意味と三角形の相似条件"}, {"id": "jp9m-ch5-l2", "title": "平行線と線分の比・中点連結定理"}, {"id": "jp9m-ch5-l3", "title": "相似比と面積比・体積比"}]}, {"id": "jp9m-ch6", "title": "円周角の定理", "lessons": [{"id": "jp9m-ch6-l1", "title": "円周角と中心角"}, {"id": "jp9m-ch6-l2", "title": "円周角の定理の利用"}, {"id": "jp9m-ch6-l3", "title": "内接四角形と接線（発展）"}]}, {"id": "jp9m-ch7", "title": "三平方の定理", "lessons": [{"id": "jp9m-ch7-l1", "title": "三平方の定理"}, {"id": "jp9m-ch7-l2", "title": "特別な直角三角形"}, {"id": "jp9m-ch7-l3", "title": "三平方の定理の利用"}]}, {"id": "jp9m-ch8", "title": "標本調査", "lessons": [{"id": "jp9m-ch8-l1", "title": "全数調査と標本調査"}, {"id": "jp9m-ch8-l2", "title": "標本から母集団を推定する"}, {"id": "jp9m-ch8-l3", "title": "標本調査の利用"}]}]')
for ch in CHAPTERS:
    for l in ch['lessons']:
        assert os.path.exists('details/%s.md' % l['id']), l['id']
    assert os.path.exists('banks/%s.txt' % ch['id']) and os.path.exists('summaries/%s.json' % ch['id']), ch['id']
ix = json.load(open('index.json', encoding='utf-8'))
entry = {'grade': 9, 'subject': 'Mathematics', 'country': 'JP', 'chapters': CHAPTERS}
done = False
for i, g in enumerate(ix['grades']):
    if g.get('country') == 'JP' and g.get('grade') == 9 and g.get('subject') == 'Mathematics':
        ix['grades'][i] = entry; done = True
if not done:
    ix['grades'].append(entry)
json.dump(ix, open('index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open('index.json', 'a').write('\n')
v = json.load(open('version.json'))
v['version'] = int(v['version']) + 1
v['updated'] = datetime.date.today().isoformat()
json.dump(v, open('version.json', 'w'))
print('JP grade 9 Mathematics: %d chapters added. version.json -> %d' % (len(CHAPTERS), v['version']))
