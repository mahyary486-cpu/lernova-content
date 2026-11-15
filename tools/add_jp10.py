#!/usr/bin/env python3
"""Adds Japan (JP) grade 10 Mathematics to index.json and bumps version.json.
Touches only the JP grade 10 Mathematics entry of the CURRENT index.json. Run from the repo root:
  python3 tools/add_jp10.py"""
import json, os, datetime
CHAPTERS = json.loads('[{"id": "jp10m-ch1", "title": "数と式", "lessons": [{"id": "jp10m-ch1-l1", "title": "式の展開と因数分解"}, {"id": "jp10m-ch1-l2", "title": "実数と絶対値・平方根"}, {"id": "jp10m-ch1-l3", "title": "一次不等式"}]}, {"id": "jp10m-ch2", "title": "集合と命題", "lessons": [{"id": "jp10m-ch2-l1", "title": "集合の要素の個数"}, {"id": "jp10m-ch2-l2", "title": "命題と条件"}, {"id": "jp10m-ch2-l3", "title": "逆・裏・対偶と証明"}]}, {"id": "jp10m-ch3", "title": "二次関数", "lessons": [{"id": "jp10m-ch3-l1", "title": "二次関数のグラフと平方完成"}, {"id": "jp10m-ch3-l2", "title": "最大・最小と式の決定"}, {"id": "jp10m-ch3-l3", "title": "二次方程式・二次不等式"}]}, {"id": "jp10m-ch4", "title": "図形と計量", "lessons": [{"id": "jp10m-ch4-l1", "title": "三角比"}, {"id": "jp10m-ch4-l2", "title": "三角比の拡張"}, {"id": "jp10m-ch4-l3", "title": "正弦定理・余弦定理と面積"}]}, {"id": "jp10m-ch5", "title": "データの分析", "lessons": [{"id": "jp10m-ch5-l1", "title": "代表値とデータの散らばり"}, {"id": "jp10m-ch5-l2", "title": "分散・標準偏差・変量の変換"}, {"id": "jp10m-ch5-l3", "title": "データの相関"}]}, {"id": "jp10m-ch6", "title": "場合の数と確率", "lessons": [{"id": "jp10m-ch6-l1", "title": "場合の数"}, {"id": "jp10m-ch6-l2", "title": "確率"}, {"id": "jp10m-ch6-l3", "title": "期待値と条件付き確率"}]}, {"id": "jp10m-ch7", "title": "図形の性質", "lessons": [{"id": "jp10m-ch7-l1", "title": "三角形の性質と五心"}, {"id": "jp10m-ch7-l2", "title": "円の性質"}, {"id": "jp10m-ch7-l3", "title": "方べきの定理と内接円・外接円"}]}, {"id": "jp10m-ch8", "title": "整数の性質", "lessons": [{"id": "jp10m-ch8-l1", "title": "約数と倍数"}, {"id": "jp10m-ch8-l2", "title": "ユークリッドの互除法とn進法"}, {"id": "jp10m-ch8-l3", "title": "整数の割り算と不定方程式"}]}]')
for ch in CHAPTERS:
    for l in ch['lessons']:
        assert os.path.exists('details/%s.md' % l['id']), l['id']
    assert os.path.exists('banks/%s.txt' % ch['id']) and os.path.exists('summaries/%s.json' % ch['id']), ch['id']
ix = json.load(open('index.json', encoding='utf-8'))
entry = {'grade': 10, 'subject': 'Mathematics', 'country': 'JP', 'chapters': CHAPTERS}
done = False
for i, g in enumerate(ix['grades']):
    if g.get('country') == 'JP' and g.get('grade') == 10 and g.get('subject') == 'Mathematics':
        ix['grades'][i] = entry; done = True
if not done:
    ix['grades'].append(entry)
json.dump(ix, open('index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open('index.json', 'a').write('\n')
v = json.load(open('version.json'))
v['version'] = int(v['version']) + 1
v['updated'] = datetime.date.today().isoformat()
json.dump(v, open('version.json', 'w'))
print('JP grade 10 Mathematics: %d chapters added. version.json -> %d' % (len(CHAPTERS), v['version']))
