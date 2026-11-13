import json, os, sys
root = os.path.expanduser("~/lernova-content")
os.chdir(root)
add = json.load(open(sys.argv[1], encoding="utf-8"))
idx = json.load(open("index.json", encoding="utf-8"))
grades = idx["grades"]
changed = 0
for entry in add:
    match = None
    for g in grades:
        if g.get("grade") == entry["grade"] and g.get("subject") == entry["subject"] and g.get("country", "US") == "US":
            match = g; break
    if match is None:
        last = max([i for i, g in enumerate(grades) if g.get("grade") == entry["grade"] and g.get("country", "US") == "US"], default=len(grades) - 1)
        match = {"grade": entry["grade"], "subject": entry["subject"], "chapters": []}
        grades.insert(last + 1, match)
        print("created: Grade %s %s" % (entry["grade"], entry["subject"]))
    have = {c["id"] for c in match["chapters"]}
    for ch in entry["chapters"]:
        if ch["id"] in have:
            print("already there, skipped:", ch["id"]); continue
        match["chapters"].append(ch); changed += 1
        print("added:", ch["id"], "-", ch["title"])
with open("index.json", "w", encoding="utf-8") as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)
print("done,", changed, "chapters added")
