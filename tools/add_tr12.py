#!/usr/bin/env python3
"""TR (Türkiye) 12. sınıf: index.json'a girişleri ekler ve version.json numarasını bir artırır.
Depo kökünde çalıştırın:  python3 tools/add_tr12.py
Tekrar çalıştırmak güvenlidir (yalnızca TR 12. sınıf girişlerini yeniden yazar)."""
import datetime, json, os
ENTRIES = [
 {
  "grade": 12,
  "subject": "Mathematics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr12m-ch1",
    "title": "Diziler",
    "lessons": [
     {
      "id": "tr12m-ch1-l1",
      "title": "Aritmetik diziler"
     },
     {
      "id": "tr12m-ch1-l2",
      "title": "Geometrik diziler ve toplamlar"
     }
    ]
   },
   {
    "id": "tr12m-ch2",
    "title": "Limit ve Süreklilik",
    "lessons": [
     {
      "id": "tr12m-ch2-l1",
      "title": "Limit"
     },
     {
      "id": "tr12m-ch2-l2",
      "title": "Süreklilik ve asimptotlar"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Physics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr12p-ch1",
    "title": "Kuvvet ve Hareket",
    "lessons": [
     {
      "id": "tr12p-ch1-l1",
      "title": "Tork, denge ve kütle merkezi"
     },
     {
      "id": "tr12p-ch1-l2",
      "title": "İtme, momentum ve açısal momentum"
     }
    ]
   },
   {
    "id": "tr12p-ch2",
    "title": "Madde ve Doğası: Modern Fizik",
    "lessons": [
     {
      "id": "tr12p-ch2-l1",
      "title": "Foton, fotoelektrik olay ve atom modelleri"
     },
     {
      "id": "tr12p-ch2-l2",
      "title": "Radyoaktivite, çekirdek tepkimeleri ve madde dalgaları"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Chemistry",
  "country": "TR",
  "chapters": [
   {
    "id": "tr12c-ch1",
    "title": "Kimya ve Elektrik",
    "lessons": [
     {
      "id": "tr12c-ch1-l1",
      "title": "Yükseltgenme–indirgenme ve galvanik piller"
     },
     {
      "id": "tr12c-ch1-l2",
      "title": "Elektroliz, korozyon ve piller"
     }
    ]
   },
   {
    "id": "tr12c-ch2",
    "title": "Karbon Kimyasına Giriş ve Organik Bileşikler",
    "lessons": [
     {
      "id": "tr12c-ch2-l1",
      "title": "Hidrokarbonlar ve izomeri"
     },
     {
      "id": "tr12c-ch2-l2",
      "title": "Fonksiyonel gruplar, polimerler ve sabun"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Science",
  "country": "TR",
  "chapters": [
   {
    "id": "tr12s-ch1",
    "title": "Kalıtım",
    "lessons": [
     {
      "id": "tr12s-ch1-l1",
      "title": "Mendel genetiği ve çaprazlamalar"
     },
     {
      "id": "tr12s-ch1-l2",
      "title": "Kan grupları, cinsiyete bağlı kalıtım ve mutasyonlar"
     }
    ]
   },
   {
    "id": "tr12s-ch2",
    "title": "Genden Proteine ve Biyoteknoloji",
    "lessons": [
     {
      "id": "tr12s-ch2-l1",
      "title": "DNA, replikasyon ve protein sentezi"
     },
     {
      "id": "tr12s-ch2-l2",
      "title": "Mutasyon ve biyoteknoloji"
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
keep = [g for g in idx['grades'] if not (g.get('country') == 'TR' and g.get('grade') == 12)]
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
print('TR 12. sınıf eklendi: %d ders, %d fasıl; version = %d' % (len(ENTRIES), sum(len(e['chapters']) for e in ENTRIES), v['version']))
