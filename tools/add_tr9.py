#!/usr/bin/env python3
"""TR (Türkiye) 9. sınıf: index.json'a girişleri ekler ve version.json numarasını bir artırır.
Depo kökünde çalıştırın:  python3 tools/add_tr9.py
Tekrar çalıştırmak güvenlidir (yalnızca TR 9. sınıf girişlerini yeniden yazar)."""
import datetime, json, os
ENTRIES = [
 {
  "grade": 9,
  "subject": "Mathematics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr9m-ch1",
    "title": "Sayılar",
    "lessons": [
     {
      "id": "tr9m-ch1-l1",
      "title": "Üslü ve köklü sayılar"
     },
     {
      "id": "tr9m-ch1-l2",
      "title": "Gerçek sayılar ve aralıklar"
     }
    ]
   },
   {
    "id": "tr9m-ch2",
    "title": "Nicelikler ve Değişimler",
    "lessons": [
     {
      "id": "tr9m-ch2-l1",
      "title": "Doğrusal fonksiyonlar ve denklemler"
     },
     {
      "id": "tr9m-ch2-l2",
      "title": "Mutlak değer ve eşitsizlikler"
     }
    ]
   }
  ]
 },
 {
  "grade": 9,
  "subject": "Physics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr9p-ch1",
    "title": "Kuvvet ve Hareket",
    "lessons": [
     {
      "id": "tr9p-ch1-l1",
      "title": "Skaler ve vektörel büyüklükler"
     },
     {
      "id": "tr9p-ch1-l2",
      "title": "Konum, yer değiştirme ve hız"
     }
    ]
   },
   {
    "id": "tr9p-ch2",
    "title": "Enerji",
    "lessons": [
     {
      "id": "tr9p-ch2-l1",
      "title": "Isı ve sıcaklık"
     },
     {
      "id": "tr9p-ch2-l2",
      "title": "Hâl değişimi ve ısı aktarımı"
     }
    ]
   }
  ]
 },
 {
  "grade": 9,
  "subject": "Chemistry",
  "country": "TR",
  "chapters": [
   {
    "id": "tr9c-ch1",
    "title": "Atom ve Periyodik Tablo",
    "lessons": [
     {
      "id": "tr9c-ch1-l1",
      "title": "Atomun yapısı ve atom modelleri"
     },
     {
      "id": "tr9c-ch1-l2",
      "title": "Periyodik tablo ve periyodik özellikler"
     }
    ]
   },
   {
    "id": "tr9c-ch2",
    "title": "Kimyasal Türler Arası Etkileşimler",
    "lessons": [
     {
      "id": "tr9c-ch2-l1",
      "title": "Güçlü etkileşimler"
     },
     {
      "id": "tr9c-ch2-l2",
      "title": "Zayıf etkileşimler"
     }
    ]
   }
  ]
 },
 {
  "grade": 9,
  "subject": "Science",
  "country": "TR",
  "chapters": [
   {
    "id": "tr9s-ch1",
    "title": "Yaşam Bilimi ve Sınıflandırma",
    "lessons": [
     {
      "id": "tr9s-ch1-l1",
      "title": "Canlıların ortak özellikleri"
     },
     {
      "id": "tr9s-ch1-l2",
      "title": "Sınıflandırma ve biyoçeşitlilik"
     }
    ]
   },
   {
    "id": "tr9s-ch2",
    "title": "Temel Bileşenler ve Hücre",
    "lessons": [
     {
      "id": "tr9s-ch2-l1",
      "title": "Canlıların temel bileşenleri"
     },
     {
      "id": "tr9s-ch2-l2",
      "title": "Hücre ve organeller"
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
keep = [g for g in idx['grades'] if not (g.get('country') == 'TR' and g.get('grade') == 9)]
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
print('TR 9. sınıf eklendi: %d ders, %d fasıl; version = %d' % (len(ENTRIES), sum(len(e['chapters']) for e in ENTRIES), v['version']))
