#!/usr/bin/env python3
"""Runs every month. When a new school year has started in a country that has lessons here, it opens an
issue as a reminder that the lessons of that country must be updated for the new year.
Old school years are never deleted.  Local test:  python3 tools/school_year.py --dry
"""
import json, os, subprocess, sys

from build_manifest import ROOT, current_label, rd

DRY = '--dry' in sys.argv


def main():
    years = rd('school_years.json', {})
    index = rd('index.json', {'grades': []})
    have = {g.get('country', 'US') for g in index.get('grades', [])}
    for cc in sorted(have):
        cfg = years.get(cc)
        if not cfg:
            continue
        now = current_label(cfg)
        if now == cfg.get('contentYear'):
            continue
        title = 'New school year %s: update the lessons of %s' % (now, cfg.get('name', cc))
        body = ('The school year %s has started in %s, but its lessons are still for %s.\n\n'
                'Add the new content, then set "contentYear" of %s to "%s" in school_years.json. '
                'The old year stays in the repository and on students\' phones until they confirm deleting it.'
                % (now, cfg.get('name', cc), cfg.get('contentYear'), cc, now))
        print(title)
        if DRY:
            continue
        found = subprocess.run(['gh', 'issue', 'list', '--state', 'open', '--search', title + ' in:title',
                                '--json', 'number'], capture_output=True, text=True, cwd=ROOT)
        if found.returncode == 0 and json.loads(found.stdout or '[]'):
            continue
        subprocess.run(['gh', 'issue', 'create', '--title', title, '--body', body], cwd=ROOT)


if __name__ == '__main__':
    main()
