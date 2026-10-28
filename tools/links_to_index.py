#!/usr/bin/env python3
"""Puts the topics of links/XX.json into index.json so the app shows them like any other country.
Every topic becomes a lesson with a 'link'. Existing real lessons are never touched."""
import json, glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f: return json.load(f)
def wr(p, d, **kw):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, **kw); f.write("\n")
index = rd("index.json"); years = rd("school_years.json"); years_changed = False
for f in sorted(glob.glob(os.path.join(ROOT, "links", "*.json"))):
    if os.path.basename(f) == "index.json": continue
    d = json.load(open(f, encoding="utf-8")); cc = d["country"]
    for g in d.get("grades", []):
        topics = [t for t in g.get("topics", []) if t.get("status") != "BROKEN"]
        if not topics: continue
        same = [x for x in index["grades"] if x.get("country") == cc and x["grade"] == g["grade"] and x["subject"] == g["subject"]]
        if any(not x.get("linkOnly") for x in same):
            print("skip (real lessons exist):", cc, g["grade"], g["subject"]); continue
        index["grades"] = [x for x in index["grades"] if x not in same]
        pre = "%s-%s%d" % (cc.lower(), g["subject"][0].lower(), g["grade"])
        lessons = [{"id": pre + "-" + re.sub(r"[^a-z0-9]+", "-", t["url"].split("/units/")[-1].split("/")[0].lower()).strip("-"),
                    "title": t["title"], "link": t["url"]} for t in topics]
        index["grades"].append({"grade": g["grade"], "country": cc, "subject": g["subject"], "linkOnly": True,
            "chapters": [{"id": pre + "-units", "title": "Official lessons - grade %d" % g["grade"], "lessons": lessons}]})
        print("added:", cc, g["grade"], g["subject"], len(lessons), "topics")
    if cc not in years:
        years[cc] = {"name": d.get("name", cc), "start": "09-01", "span": 2, "contentYear": "2026-2027"}; years_changed = True; print("school year added:", cc)
wr("index.json", index, indent=2)
if years_changed: wr("school_years.json", years, indent=2)
