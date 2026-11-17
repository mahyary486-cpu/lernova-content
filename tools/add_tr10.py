#!/usr/bin/env python3
"""TR (Türkiye) 10. sınıf: index.json'a girişleri ekler ve version.json numarasını bir artırır.
Depo kökünde çalıştırın:  python3 tools/add_tr10.py
Tekrar çalıştırmak güvenlidir (yalnızca TR 10. sınıf girişlerini yeniden yazar)."""
import datetime, json, os
ENTRIES = [
 {
  "grade": 10,
  "subject": "Mathematics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr10m-ch1",
    "title": "Karesel Fonksiyonlar, Denklemler ve Eşitsizlikler",
    "lessons": [
     {
      "id": "tr10m-ch1-l1",
      "title": "İkinci dereceden denklemler ve kökler"
     },
     {
      "id": "tr10m-ch1-l2",
      "title": "Karesel fonksiyon, eşitsizlik, karekök ve rasyonel ifadeler"
     }
    ]
   },
   {
    "id": "tr10m-ch2",
    "title": "Sayma Stratejileri ve Olasılık",
    "lessons": [
     {
      "id": "tr10m-ch2-l1",
      "title": "Sayma stratejileri: permütasyon ve kombinasyon"
     },
     {
      "id": "tr10m-ch2-l2",
      "title": "Olasılık ve koşullu olasılık"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Physics",
  "country": "TR",
  "chapters": [
   {
    "id": "tr10p-ch1",
    "title": "Elektrik",
    "lessons": [
     {
      "id": "tr10p-ch1-l1",
      "title": "Elektrik yükü ve elektrik akımı"
     },
     {
      "id": "tr10p-ch1-l2",
      "title": "Direnç, devreler ve elektriksel enerji"
     }
    ]
   },
   {
    "id": "tr10p-ch2",
    "title": "Dalgalar",
    "lessons": [
     {
      "id": "tr10p-ch2-l1",
      "title": "Dalga türleri ve temel özellikleri"
     },
     {
      "id": "tr10p-ch2-l2",
      "title": "Yansıma, kırılma ve ses"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Chemistry",
  "country": "TR",
  "chapters": [
   {
    "id": "tr10c-ch1",
    "title": "Çözeltiler",
    "lessons": [
     {
      "id": "tr10c-ch1-l1",
      "title": "Çözünme süreci ve derişim birimleri"
     },
     {
      "id": "tr10c-ch1-l2",
      "title": "Çözünürlük ve koligatif özellikler"
     }
    ]
   },
   {
    "id": "tr10c-ch2",
    "title": "Kimyasal Tepkimeler ve Yeşil Kimya",
    "lessons": [
     {
      "id": "tr10c-ch2-l1",
      "title": "Mol kavramı ve kimyasal tepkimeler"
     },
     {
      "id": "tr10c-ch2-l2",
      "title": "Yeşil kimya ve sürdürülebilirlik"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Science",
  "country": "TR",
  "chapters": [
   {
    "id": "tr10s-ch1",
    "title": "Enerji, ATP ve Solunum",
    "lessons": [
     {
      "id": "tr10s-ch1-l1",
      "title": "ATP ve canlılarda enerji dönüşümü"
     },
     {
      "id": "tr10s-ch1-l2",
      "title": "Hücresel solunum ve fermantasyon"
     }
    ]
   },
   {
    "id": "tr10s-ch2",
    "title": "Fotosentez ve Ekoloji",
    "lessons": [
     {
      "id": "tr10s-ch2-l1",
      "title": "Fotosentez"
     },
     {
      "id": "tr10s-ch2-l2",
      "title": "Ekosistem ekolojisi ve madde döngüleri"
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
keep = [g for g in idx['grades'] if not (g.get('country') == 'TR' and g.get('grade') == 10)]
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
print('TR 10. sınıf eklendi: %d ders, %d fasıl; version = %d' % (len(ENTRIES), sum(len(e['chapters']) for e in ENTRIES), v['version']))
