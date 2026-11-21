#!/usr/bin/env python3
"""version.json numarasını bir artırır (içerik güncellemesinin uygulamaya yansıması için)."""
import datetime, json, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
v = json.load(open('version.json'))
v['version'] = int(v['version']) + 1
v['updated'] = datetime.date.today().isoformat()
open('version.json', 'w', encoding='utf-8').write(json.dumps(v, indent=1) + '\n')
print('version =', v['version'])
