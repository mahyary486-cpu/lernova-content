#!/usr/bin/env python3
"""TR (Türkiye) 11. sınıf: index.json'a girişleri ekler ve version.json numarasını bir artırır.
Depo kökünde çalıştırın:  python3 tools/add_tr11.py
Tekrar çalıştırmak güvenlidir (yalnızca TR 11. sınıf girişlerini yeniden yazar)."""
import datetime, json, os
ENTRIES = [
 {
  "grade": 11,
  "subject": "Mathematics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr11m-ch1",
    "title": "Geometrik Şekiller",
    "lessons": [
     {
      "id": "tr11m-ch1-l1",
      "title": "Dörtgenler ve özel dörtgenler"
     },
     {
      "id": "tr11m-ch1-l2",
      "title": "Çokgenler"
     }
    ]
   },
   {
    "id": "tr11m-ch2",
    "title": "Nicelikler ve Değişimler",
    "lessons": [
     {
      "id": "tr11m-ch2-l1",
      "title": "Trigonometrik fonksiyonlar"
     },
     {
      "id": "tr11m-ch2-l2",
      "title": "Üstel ve logaritmik fonksiyonlar, bileşke"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Physics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr11p-ch1",
    "title": "Kuvvet ve Hareket",
    "lessons": [
     {
      "id": "tr11p-ch1-l1",
      "title": "Newton'un hareket yasaları ve sürtünme"
     },
     {
      "id": "tr11p-ch1-l2",
      "title": "Limit hız ve çembersel hareket"
     }
    ]
   },
   {
    "id": "tr11p-ch2",
    "title": "Optik",
    "lessons": [
     {
      "id": "tr11p-ch2-l1",
      "title": "Aydınlanma ve aynalar"
     },
     {
      "id": "tr11p-ch2-l2",
      "title": "Işığın kırılması, prizmalar ve fiber optik"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Chemistry",
  "country": "TR",
  "chapters": [
   {
    "id": "tr11c-ch1",
    "title": "Kimyasal Tepkimelerde Enerji ve Hız",
    "lessons": [
     {
      "id": "tr11c-ch1-l1",
      "title": "Kimyasal tepkimelerde enerji"
     },
     {
      "id": "tr11c-ch1-l2",
      "title": "Kimyasal tepkimelerde hız"
     }
    ]
   },
   {
    "id": "tr11c-ch2",
    "title": "Kimyasal Denge",
    "lessons": [
     {
      "id": "tr11c-ch2-l1",
      "title": "Kimyasal denge ve Le Chatelier ilkesi"
     },
     {
      "id": "tr11c-ch2-l2",
      "title": "Asit–baz dengesi ve çözünürlük dengesi"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Science",
  "country": "TR",
  "chapters": [
   {
    "id": "tr11s-ch1",
    "title": "Tepki",
    "lessons": [
     {
      "id": "tr11s-ch1-l1",
      "title": "Bitkilerde tepki"
     },
     {
      "id": "tr11s-ch1-l2",
      "title": "Hayvanlarda tepki: sinir sistemi, kas-iskelet ve bağışıklık"
     }
    ]
   },
   {
    "id": "tr11s-ch2",
    "title": "Homeostazi",
    "lessons": [
     {
      "id": "tr11s-ch2-l1",
      "title": "Homeostazi, endokrin sistem ve dolaşım"
     },
     {
      "id": "tr11s-ch2-l2",
      "title": "Solunum, boşaltım ve iç dengenin korunması"
     }
    ]
   }
  ]
 }
]
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
raw = open('index.json', encoding='utf-8').read()
idx = json.loads(raw)
asc = json.dumps(idx, ensure_ascii=True, indent=2) == raw.strip()
keep = [g for g in idx['grades'] if not (g.get('country') == 'TR' and g.get('grade') == 11)]
mine = {(e['grade'], e['subject']) for e in ENTRIES}
idx['grades'] = keep + ENTRIES
out = json.dumps(idx, ensure_ascii=asc, indent=2)
v = json.load(open('version.json'))
if out != raw.strip():
    open('index.json', 'w', encoding='utf-8').write(out + ('\n' if raw.endswith('\n') else ''))
    v['version'] = int(v['version']) + 1
    v['updated'] = datetime.date.today().isoformat()
    open('version.json', 'w', encoding='utf-8').write(json.dumps(v, indent=1) + '\n')
else:
    print('(index.json zaten güncel، version تغییر نکرد)')
print('TR 11. sınıf eklendi: %d ders, %d fasıl; version = %d' % (len(ENTRIES), sum(len(e['chapters']) for e in ENTRIES), v['version']))
