#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Register the French (FR) grades/chapters/lessons in index.json.

The bot (tools/build_manifest.py) builds packs/FR.json and manifest.json from index.json,
so this script ONLY touches index.json, and ONLY the entries with country == "FR".
Run from the repo root:  python3 tools/fr_index.py   (safe to run several times)
"""
import glob, json, os, sys

ROOT = os.getcwd()
PARTS = sorted(glob.glob(os.path.join(ROOT, "tools", "fr_*_part.json")))
IDX = os.path.join(ROOT, "index.json")
if not PARTS or not os.path.exists(IDX):
    sys.exit("Run from the repo root (index.json and tools/fr_*_part.json needed).")

raw = open(IDX, encoding="utf-8").read()
data = json.loads(raw)

# find the formatting used by the file so the diff stays minimal
fmt = None
for indent in (2, 1, 4, None):
    for ea in (False, True):
        for nl in ("\n", ""):
            kw = {"indent": indent, "ensure_ascii": ea}
            if indent is None:
                kw["separators"] = (",", ":")
            if json.dumps(data, **kw) + nl == raw:
                fmt = (kw, nl)
                break
        if fmt: break
    if fmt: break
if fmt is None:
    print("Warning: unknown index.json formatting, using indent=2 (the diff may be large).")
    fmt = ({"indent": 2, "ensure_ascii": False}, "\n")

grades = data["grades"]
changed = 0
for p in PARTS:
    part = json.load(open(p, encoding="utf-8"))
    for new in part["grades"]:
        pos = [i for i, g in enumerate(grades)
               if g.get("country") == "FR" and g.get("grade") == new["grade"] and g.get("subject") == new["subject"]]
        fr_all = [i for i, g in enumerate(grades) if g.get("country") == "FR"]
        # keep the key order of an existing FR entry
        order = list(grades[fr_all[0]].keys()) if fr_all else ["grade", "subject", "chapters", "country"]
        entry = {k: new[k] for k in order if k in new}
        entry.update({k: v for k, v in new.items() if k not in entry})
        if pos:
            if grades[pos[0]] != entry:
                grades[pos[0]] = entry; changed += 1
        else:
            at = (max(fr_all) + 1) if fr_all else len(grades)
            grades.insert(at, entry); changed += 1

if changed:
    with open(IDX, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(data, **fmt[0]) + fmt[1])
fr = [(g["grade"], g["subject"], len(g["chapters"])) for g in grades if g.get("country") == "FR"]
print("index.json: %d change(s). FR entries: %s" % (changed, fr))
