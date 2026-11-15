import json, os, re, sys
root = os.path.expanduser("~/lernova-content")
os.chdir(root)
idx = json.load(open("index.json", encoding="utf-8"))
def stats(path):
    t = open(path, encoding="utf-8").read()
    words = len(t.split())
    prose = [l for l in t.splitlines() if l.strip() and not re.match(r"\s*(#|-|\d+\.|\*\*Example)", l)]
    pw = sum(len(l.split()) for l in prose)
    bul = sum(1 for l in t.splitlines() if l.lstrip().startswith("-"))
    return words, len(prose), pw, bul
out = []; flagged = []
tot = 0; totflag = 0
for g in idx["grades"]:
    key = "%s | %s | grade %s" % (g.get("country", "US"), g.get("subject"), g.get("grade"))
    n = 0; w = 0; f = 0
    for ch in g["chapters"]:
        for l in ch["lessons"]:
            p = "details/%s.md" % l["id"]
            if not os.path.exists(p):
                flagged.append((l["id"], "missing")); f += 1; n += 1; continue
            words, nprose, pw, bul = stats(p)
            n += 1; w += words
            if words < 450 or pw < 120:
                f += 1; flagged.append((l["id"], "words=%d prose_words=%d bullets=%d" % (words, pw, bul)))
    out.append("%-40s lessons=%3d avg_words=%4d thin=%3d" % (key, n, w // max(n, 1), f))
    tot += n; totflag += f
print("\n".join(out))
print("\nTOTAL lessons=%d thin=%d" % (tot, totflag))
open("/tmp/thin_lessons.txt", "w").write("\n".join("%s  %s" % x for x in flagged) + "\n")
print("list of thin lessons: /tmp/thin_lessons.txt")
