#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the French (FR) content into the Lernova content repo.

Run from the repo root:  python3 tools/fr_merge.py
It only touches: packs/FR.json and the "FR" entry of manifest.json.
Other countries are never modified. Safe to run several times.
"""
import hashlib, json, os, sys

ROOT = os.getcwd()
PART = os.path.join(ROOT, "tools", "fr_math9_part.json")
if not os.path.exists(PART):
    sys.exit("Run this script from the repo root (tools/fr_math9_part.json not found).")

def read(p):
    with open(p, "rb") as f:
        return f.read()

part = json.loads(read(PART).decode("utf-8"))
year = part["year"]

pack_path = os.path.join(ROOT, "packs", "FR.json")
os.makedirs(os.path.dirname(pack_path), exist_ok=True)
if os.path.exists(pack_path):
    pack = json.loads(read(pack_path).decode("utf-8"))
else:
    pack = {"country": "FR", "files": {}, "year": year, "rev": "", "grades": []}
if str(pack.get("year")) != year:
    print("Note: pack year changes", pack.get("year"), "->", year)
    pack = {"country": "FR", "files": {}, "year": year, "rev": "", "grades": []}

keep = [g for g in pack.get("grades", [])
        if not any(g.get("grade") == n["grade"] and g.get("subject") == n["subject"] for n in part["grades"])]
pack["grades"] = keep + part["grades"]
pack["grades"].sort(key=lambda g: (g["grade"], g["subject"]))

files = dict(pack.get("files", {}))
for g in part["grades"]:
    for ch in g["chapters"]:
        for path in (f"banks/{ch['id']}.txt", f"summaries/{ch['id']}.json"):
            files[path] = hashlib.sha1(read(os.path.join(ROOT, path))).hexdigest()[:10]
        for ls in ch["lessons"]:
            path = f"details/{ls['id']}.md"
            files[path] = hashlib.sha1(read(os.path.join(ROOT, path))).hexdigest()[:10]
pack["files"] = dict(sorted(files.items()))
pack["country"] = "FR"
pack["year"] = year
pack["rev"] = hashlib.sha1(json.dumps(pack["files"], sort_keys=True).encode()).hexdigest()[:10]

with open(pack_path, "w", encoding="utf-8", newline="\n") as f:
    json.dump(pack, f, ensure_ascii=False, separators=(",", ":"))
    f.write("\n")

man_path = os.path.join(ROOT, "manifest.json")
indent = 2
if os.path.exists(man_path):
    raw = read(man_path).decode("utf-8")
    man = json.loads(raw)
    indent = 2 if "\n  " in raw else None
else:
    man = {}
man.setdefault("countries", {})
size = sum(os.path.getsize(os.path.join(ROOT, p)) for p in pack["files"]) + os.path.getsize(pack_path)
entry = dict(man["countries"].get("FR", {}))
entry.update({"year": year, "rev": pack["rev"], "bytes": size})
man["countries"]["FR"] = entry
with open(man_path, "w", encoding="utf-8", newline="\n") as f:
    if indent:
        json.dump(man, f, ensure_ascii=False, indent=indent)
    else:
        json.dump(man, f, ensure_ascii=False, separators=(",", ":"))
    f.write("\n")

print("FR pack OK: %d files, rev %s, %.1f KB" % (len(pack["files"]), pack["rev"], size / 1024))
