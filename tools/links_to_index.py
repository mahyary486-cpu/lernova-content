#!/usr/bin/env python3
"""Puts the topics of links/XX.json into index.json so the app shows them like any other country.
Every topic becomes its own chapter (so it can have its own exam bank) with one lesson that has a 'link'.
Real lessons are never touched; only grades marked linkOnly are rebuilt."""
import json, glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f: return json.load(f)
def wr(p, d, **kw):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, **kw); f.write("\n")
def slug(url):
    s = url.split("/units/")[-1].split("/")[0].lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
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
        chapters = []
        for t in topics:
            cid = pre + "-" + slug(t["url"])
            chapters.append({"id": cid, "title": t["title"], "lessons": [{"id": cid + "-l1", "title": t["title"], "link": t["url"]}]})
        index["grades"].append({"grade": g["grade"], "country": cc, "subject": g["subject"], "linkOnly": True, "chapters": chapters})
        print("added:", cc, g["grade"], g["subject"], len(chapters), "topics")
    if cc not in years:
        years[cc] = {"name": d.get("name", cc), "start": "09-01", "span": 2, "contentYear": "2026-2027"}; years_changed = True; print("school year added:", cc)
wr("index.json", index, indent=2)
if years_changed: wr("school_years.json", years, indent=2)
