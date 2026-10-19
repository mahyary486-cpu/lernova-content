#!/usr/bin/env python3
"""Builds manifest.json and packs/<COUNTRY>.json for the Lernova app.

manifest.json  - tiny list of countries (revision, school year, size). The app reads this first.
packs/XX.json  - everything the app needs for one country: its grades/chapters/lessons and the
                 fingerprint of every file, so the app downloads only what changed.
Nothing is ever deleted from the content folders. Run:  python3 tools/build_manifest.py
"""
import datetime, hashlib, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rd(path, default=None):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return default
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def fp(path):
    with open(os.path.join(ROOT, path), 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()[:10]


def current_label(cfg, today=None):
    """School year that is running today for a country, e.g. 2026-2027 (or 2027 for one-year countries)."""
    today = today or datetime.date.today()
    m, d = [int(x) for x in cfg.get('start', '09-01').split('-')]
    begin = today.year if today >= datetime.date(today.year, m, d) else today.year - 1
    return '%d-%d' % (begin, begin + 1) if cfg.get('span', 2) == 2 else '%d' % begin


def build():
    index = rd('index.json', {'grades': []})
    years = rd('school_years.json', {})
    by_country = {}
    for g in index.get('grades', []):
        by_country.setdefault(g.get('country', 'US'), []).append(g)

    os.makedirs(os.path.join(ROOT, 'packs'), exist_ok=True)
    manifest = {'countries': {}}
    for cc in sorted(by_country):
        cfg = years.get(cc, {})
        year = cfg.get('contentYear', '2026-2027')
        grades = [g for g in by_country[cc] if g.get('year', year) == year]
        files = {}
        for g in grades:
            for c in g.get('chapters', []):
                cid = c['id']
                for rel in ('summaries/%s.json' % cid, 'banks/%s.txt' % cid):
                    if os.path.exists(os.path.join(ROOT, rel)):
                        files[rel] = fp(rel)
                for l in c.get('lessons', []):
                    rel = 'details/%s.md' % l['id']
                    if os.path.exists(os.path.join(ROOT, rel)):
                        files[rel] = fp(rel)
        size = sum(os.path.getsize(os.path.join(ROOT, p)) for p in files)
        rev = hashlib.sha1(
            (json.dumps(files, sort_keys=True) + json.dumps(grades, sort_keys=True)).encode('utf-8')
        ).hexdigest()[:10]
        pack = {'country': cc, 'year': year, 'rev': rev, 'grades': grades, 'files': files}
        with open(os.path.join(ROOT, 'packs', cc + '.json'), 'w', encoding='utf-8') as f:
            json.dump(pack, f, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        manifest['countries'][cc] = {
            'name': cfg.get('name', cc), 'year': year,
            'currentYear': current_label(cfg) if cfg else year,
            'rev': rev, 'bytes': size, 'files': len(files),
        }
    with open(os.path.join(ROOT, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, sort_keys=True, indent=1)
    for cc, m in manifest['countries'].items():
        print('%s  year %s  files %d  %.1f MB  rev %s' % (cc, m['year'], m['files'], m['bytes'] / 1048576, m['rev']))


if __name__ == '__main__':
    build()
