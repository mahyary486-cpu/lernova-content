#!/usr/bin/env python3
"""Checks every link in links/*.json. Only a real 404/410 is BROKEN; other errors are UNKNOWN."""
import json, glob, urllib.request, urllib.error, datetime
for f in sorted(glob.glob("links/*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for e in d["entries"]:
        try:
            urllib.request.urlopen(urllib.request.Request(e["url"], headers={"User-Agent": "Mozilla/5.0"}), timeout=30)
            e["status"] = "OK"
        except urllib.error.HTTPError as x:
            e["status"] = "BROKEN" if x.code in (404, 410) else "UNKNOWN(%s)" % x.code
        except Exception:
            e["status"] = "UNKNOWN"
        e["checked"] = str(datetime.date.today())
        print(d["country"], e["subject"], "->", e["status"])
    json.dump(d, open(f, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
