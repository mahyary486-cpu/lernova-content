#!/usr/bin/env python3
"""Checks every url in links/*.json (only 404/410 = BROKEN) and writes links/index.json."""
import json, glob, os, urllib.request, urllib.error, datetime
def check(o):
    try:
        urllib.request.urlopen(urllib.request.Request(o["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=30)
        o["status"] = "OK"
    except urllib.error.HTTPError as x:
        o["status"] = "BROKEN" if x.code in (404, 410) else "UNKNOWN(%s)" % x.code
    except Exception:
        o["status"] = "UNKNOWN"
    o["checked"] = str(datetime.date.today())
    print(o["status"], "-", o.get("title", o["url"])[:60])
def walk(o):
    if isinstance(o, dict):
        if "url" in o: check(o)
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for x in o: walk(x)
codes = []
for f in sorted(glob.glob("links/*.json")):
    if os.path.basename(f) == "index.json": continue
    d = json.load(open(f, encoding="utf-8"))
    walk(d)
    json.dump(d, open(f, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    codes.append(d["country"])
json.dump({"countries": codes}, open("links/index.json", "w"), indent=1)
print("link countries:", codes)
