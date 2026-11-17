#!/usr/bin/env python3
"""TJ (Tajikistan) grades 9-12: adds the entries to index.json, TJ to school_years.json, and adds 1 to version.json.
Run from the repo root:  python3 tools/add_tj.py   (safe to run twice; it only rewrites the TJ entries)"""
import datetime, json
ENTRIES = [
 {
  "grade": 9,
  "subject": "Mathematics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj9m-ch1",
    "title": "Муодилаҳо ва нобаробарӣҳо",
    "lessons": [
     {
      "id": "tj9m-ch1-l1",
      "title": "Муодилаи квадратӣ"
     },
     {
      "id": "tj9m-ch1-l2",
      "title": "Нобаробарӣҳои квадратӣ"
     }
    ]
   },
   {
    "id": "tj9m-ch2",
    "title": "Прогрессияҳо",
    "lessons": [
     {
      "id": "tj9m-ch2-l1",
      "title": "Прогрессияи арифметикӣ"
     },
     {
      "id": "tj9m-ch2-l2",
      "title": "Прогрессияи геометрӣ"
     }
    ]
   }
  ]
 },
 {
  "grade": 9,
  "subject": "Physics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj9p-ch1",
    "title": "Кинематика",
    "lessons": [
     {
      "id": "tj9p-ch1-l1",
      "title": "Ҳаракати якҷинсаи рост"
     },
     {
      "id": "tj9p-ch1-l2",
      "title": "Ҳаракати баробартезшаванда"
     }
    ]
   },
   {
    "id": "tj9p-ch2",
    "title": "Динамика",
    "lessons": [
     {
      "id": "tj9p-ch2-l1",
      "title": "Қонунҳои Нютон"
     },
     {
      "id": "tj9p-ch2-l2",
      "title": "Қувваҳо дар табиат"
     }
    ]
   }
  ]
 },
 {
  "grade": 9,
  "subject": "Chemistry",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj9c-ch1",
    "title": "Электролитҳо ва диссотсиатсия",
    "lessons": [
     {
      "id": "tj9c-ch1-l1",
      "title": "Диссотсиатсияи электролитӣ"
     },
     {
      "id": "tj9c-ch1-l2",
      "title": "Реаксияҳои мубодилаи ионӣ"
     }
    ]
   },
   {
    "id": "tj9c-ch2",
    "title": "Ғайрифилизот",
    "lessons": [
     {
      "id": "tj9c-ch2-l1",
      "title": "Галогенҳо ва хлориди гидроген"
     },
     {
      "id": "tj9c-ch2-l2",
      "title": "Сулфур ва ҳосилаҳои он"
     }
    ]
   }
  ]
 },
 {
  "grade": 9,
  "subject": "Biology",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj9b-ch1",
    "title": "Асосҳои генетика",
    "lessons": [
     {
      "id": "tj9b-ch1-l1",
      "title": "Қонунҳои Мендел"
     },
     {
      "id": "tj9b-ch1-l2",
      "title": "Ирсият ва тағйирёбандӣ"
     }
    ]
   },
   {
    "id": "tj9b-ch2",
    "title": "Ҳуҷайра ва тақсимшавӣ",
    "lessons": [
     {
      "id": "tj9b-ch2-l1",
      "title": "Сохти ҳуҷайра"
     },
     {
      "id": "tj9b-ch2-l2",
      "title": "Митоз ва мейоз"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Mathematics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj10m-ch1",
    "title": "Тригонометрия",
    "lessons": [
     {
      "id": "tj10m-ch1-l1",
      "title": "Арзишҳои тригонометрӣ"
     },
     {
      "id": "tj10m-ch1-l2",
      "title": "Формулаҳои асосии тригонометрӣ"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Physics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj10p-ch1",
    "title": "Физикаи молекулавӣ ва термодинамика",
    "lessons": [
     {
      "id": "tj10p-ch1-l1",
      "title": "Қонунҳои гази идеалӣ"
     },
     {
      "id": "tj10p-ch1-l2",
      "title": "Термодинамика"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Chemistry",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj10c-ch1",
    "title": "Кимиёи органикӣ",
    "lessons": [
     {
      "id": "tj10c-ch1-l1",
      "title": "Алканҳо"
     },
     {
      "id": "tj10c-ch1-l2",
      "title": "Спиртҳо ва кислотаҳои карбон"
     }
    ]
   }
  ]
 },
 {
  "grade": 10,
  "subject": "Biology",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj10b-ch1",
    "title": "Асосҳои биохимияи ирсият",
    "lessons": [
     {
      "id": "tj10b-ch1-l1",
      "title": "ДНК ва РНК"
     },
     {
      "id": "tj10b-ch1-l2",
      "title": "Синтези сафеда"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Mathematics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj11m-ch1",
    "title": "Ҳосила",
    "lessons": [
     {
      "id": "tj11m-ch1-l1",
      "title": "Ҳосили функсия"
     },
     {
      "id": "tj11m-ch1-l2",
      "title": "Татбиқи ҳосила"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Physics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj11p-ch1",
    "title": "Электродинамика",
    "lessons": [
     {
      "id": "tj11p-ch1-l1",
      "title": "Қонуни Ом"
     },
     {
      "id": "tj11p-ch1-l2",
      "title": "Кори ҷараён ва қонуни Кулон"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Chemistry",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj11c-ch1",
    "title": "Металлҳо",
    "lessons": [
     {
      "id": "tj11c-ch1-l1",
      "title": "Қатори фаъолии металлҳо"
     },
     {
      "id": "tj11c-ch1-l2",
      "title": "Зангзанӣ ва электролиз"
     }
    ]
   }
  ]
 },
 {
  "grade": 11,
  "subject": "Biology",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj11b-ch1",
    "title": "Эволютсия",
    "lessons": [
     {
      "id": "tj11b-ch1-l1",
      "title": "Назарияи Дарвин"
     },
     {
      "id": "tj11b-ch1-l2",
      "title": "Далелҳо ва шаклҳои эволютсия"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Mathematics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj12m-ch1",
    "title": "Интеграл",
    "lessons": [
     {
      "id": "tj12m-ch1-l1",
      "title": "Интеграли номуайян"
     },
     {
      "id": "tj12m-ch1-l2",
      "title": "Интеграли муайян ва масоҳат"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Physics",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj12p-ch1",
    "title": "Оптика ва физикаи атомӣ",
    "lessons": [
     {
      "id": "tj12p-ch1-l1",
      "title": "Оптикаи геометрӣ"
     },
     {
      "id": "tj12p-ch1-l2",
      "title": "Радиоактивӣ"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Chemistry",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj12c-ch1",
    "title": "Ҳисобҳои кимиёвӣ ва мувозинат",
    "lessons": [
     {
      "id": "tj12c-ch1-l1",
      "title": "Консентратсияи маҳлул"
     },
     {
      "id": "tj12c-ch1-l2",
      "title": "pH ва мувозинати кимиёвӣ"
     }
    ]
   }
  ]
 },
 {
  "grade": 12,
  "subject": "Biology",
  "country": "TJ",
  "chapters": [
   {
    "id": "tj12b-ch1",
    "title": "Экология",
    "lessons": [
     {
      "id": "tj12b-ch1-l1",
      "title": "Экосистема ва занҷири ғизоӣ"
     },
     {
      "id": "tj12b-ch1-l2",
      "title": "Популятсия ва муҳофизати табиат"
     }
    ]
   }
  ]
 }
]
ix = json.load(open('index.json', encoding='utf-8'))
ix['grades'] = [g for g in ix['grades'] if g.get('country') != 'TJ'] + ENTRIES
json.dump(ix, open('index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sy = json.load(open('school_years.json', encoding='utf-8'))
sy.setdefault('TJ', {'name': 'Tajikistan', 'start': '09-01', 'span': 2, 'contentYear': '2026-2027'})
json.dump(sy, open('school_years.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
v = json.load(open('version.json'))
v['version'] = int(v['version']) + 1
v['updated'] = datetime.date.today().isoformat()
json.dump(v, open('version.json', 'w'), indent=1)
print('TJ grades 9-12 added. version =', v['version'])
