import json, os, re, sys, collections

ROOT = os.path.expanduser("~/lernova-content") if len(sys.argv) < 2 else sys.argv[1]
os.chdir(ROOT)

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

idx = load("index.json")
issues = []
rows = []
seen_ids = set()

def check_bank(ch):
    p = "banks/%s.txt" % ch
    if not os.path.exists(p):
        return None, ["bank file missing"]
    lines = [l for l in open(p, encoding="utf-8").read().split("\n") if l.strip()]
    probs = []
    if not lines or not lines[0].startswith("#"):
        return None, ["bank has no header line"]
    header = lines[0][1:].strip()
    qs = lines[1:]
    if len(qs) != 50:
        probs.append("%d questions (expected 50)" % len(qs))
    if len(header) != len(qs):
        probs.append("header length %d but %d questions" % (len(header), len(qs)))
    if set(header) - set("EMH"):
        probs.append("header has characters other than E/M/H")
    keys = {}
    positions = collections.Counter()
    for i, l in enumerate(qs, 1):
        f = l.split("|")
        if len(f) != 7:
            probs.append("question %d has %d fields (expected 7)" % (i, len(f))); continue
        q, o, idx_s, ex = f[0], f[1:5], f[5], f[6]
        if idx_s not in ("0", "1", "2", "3"):
            probs.append("question %d bad answer index %r" % (i, idx_s)); continue
        if any(not x.strip() for x in o) or len(set(o)) != 4:
            probs.append("question %d options empty or repeated" % i)
        if not ex.strip():
            probs.append("question %d has no explanation" % i)
        positions[int(idx_s)] += 1
        k = q + "\n" + o[int(idx_s)]
        if q in [x.split("\n")[0] for x in keys]:
            probs.append("question %d is a duplicate" % i)
        keys[k] = i
    if positions and max(positions.values()) > 20:
        probs.append("answer positions unbalanced %s" % dict(positions))
    return keys, probs

def check_solutions(ch, keys):
    p = "solutions/%s.json" % ch
    if not os.path.exists(p):
        return ["solutions file missing"]
    try:
        d = load(p)
    except Exception as e:
        return ["solutions file is not valid JSON"]
    probs = []
    missing = [k for k in keys if k not in d]
    extra = [k for k in d if k not in keys]
    if missing:
        probs.append("%d bank questions have no solution" % len(missing))
    if extra:
        probs.append("%d solutions match no bank question" % len(extra))
    weak = [k for k, v in d.items() if "1)" not in v]
    if weak:
        probs.append("%d solutions have no numbered steps" % len(weak))
    return probs

summary = collections.OrderedDict()
for g in idx["grades"]:
    if g.get("country", "US") != "US":
        continue
    label = "Grade %s %s" % (g["grade"], g["subject"])
    st = summary.setdefault(label, dict(ch=0, lessons=0, sumok=0, detok=0, bankok=0, solok=0))
    for c in g["chapters"]:
        cid = c["id"]; seen_ids.add(cid)
        st["ch"] += 1
        problems = []
        # summary layer
        sp = "summaries/%s.json" % cid
        okS = False
        if not os.path.exists(sp):
            problems.append("summary file missing")
        else:
            try:
                sd = load(sp)
                miss = [l["title"] for l in c["lessons"] if l["title"] not in sd]
                if miss:
                    problems.append("summary missing for lessons: %s" % "; ".join(miss))
                else:
                    okS = True
            except Exception:
                problems.append("summary file is not valid JSON")
        # detailed layer
        okD = True
        for l in c["lessons"]:
            st["lessons"] += 1
            dp = "details/%s.md" % l["id"]
            if not os.path.exists(dp) or os.path.getsize(dp) < 300:
                okD = False
                problems.append("detailed text missing or too short: %s" % l["id"])
        # bank + solutions
        keys, bp = check_bank(cid)
        problems += bp
        okB = keys is not None and not bp
        okSol = False
        if keys is not None:
            sp2 = check_solutions(cid, keys)
            problems += sp2
            okSol = not sp2
        st["sumok"] += okS; st["detok"] += okD; st["bankok"] += okB; st["solok"] += okSol
        if problems:
            issues.append((label, cid, c["title"], problems))

print("=" * 60)
print("US CONTENT REPORT")
print("=" * 60)
print("%-34s %4s %7s %5s %5s %5s %5s" % ("Subject", "Ch", "Lessons", "Summ", "Detl", "Bank", "Soln"))
for k, s in summary.items():
    print("%-34s %4d %7d %5d %5d %5d %5d" % (k, s["ch"], s["lessons"], s["sumok"], s["detok"], s["bankok"], s["solok"]))
print()

# what is still to build
plan = {"9": ("Mathematics", 7), "10": ("Mathematics", 7), "11": ("Mathematics", 8), "12": ("Mathematics", 8)}
prefix_plan = {}
for g in ("9", "10", "11", "12"):
    prefix_plan["g%sp" % g] = ("Physics grade " + g, 5)
    prefix_plan["g%sc" % g] = ("Chemistry grade " + g, 5)
have = collections.Counter()
for cid in seen_ids:
    m = re.match(r"^(g\d+[pc]?)-ch\d+$", cid)
    if m: have[m.group(1)] += 1
print("PLAN CHECK (chapters present in index / planned)")
for g, (name, n) in (("g9", ("Mathematics grade 9", 7)), ("g10", ("Mathematics grade 10", 7)),
                     ("g11", ("Mathematics grade 11", 8)), ("g12", ("Mathematics grade 12", 8))):
    print("  %-24s %d / %d%s" % (name, have[g], n, "" if have[g] >= n else "   <-- INCOMPLETE"))
for pre, (name, n) in prefix_plan.items():
    print("  %-24s %d / %d%s" % (name, have[pre], n, "" if have[pre] >= n else "   <-- INCOMPLETE"))
print()

# stray files
stray = []
for folder, ext in (("banks", ".txt"), ("summaries", ".json"), ("solutions", ".json")):
    for f in sorted(os.listdir(folder)):
        m = re.match(r"^(g\d+[pc]?-ch\d+)" + re.escape(ext) + "$", f)
        if m and m.group(1) not in seen_ids:
            stray.append("%s/%s" % (folder, f))
for f in sorted(os.listdir("details")):
    m = re.match(r"^(g\d+[pc]?-ch\d+)-l\d+\.md$", f)
    if m and m.group(1) not in seen_ids:
        stray.append("details/" + f)
if stray:
    print("FILES NOT LISTED IN index.json (%d):" % len(stray))
    for s in stray[:60]: print("  " + s)
    print()

if issues:
    print("PROBLEMS FOUND (%d chapters)" % len(issues))
    for label, cid, title, probs in issues:
        print("- %s / %s (%s)" % (label, cid, title))
        for p in probs[:8]: print("    * " + p)
        if len(probs) > 8: print("    * ... %d more" % (len(probs) - 8))
else:
    print("NO PROBLEMS FOUND in any US chapter listed in index.json")
