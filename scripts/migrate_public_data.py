#!/usr/bin/env python3
"""One-off, idempotent: rewrite the committed data files to the public format written by scripts/verify.py.
- data/tools.json: public_tool() rows (public status, data fields, check names without notes).
- data/verification-report.json: run date, counts by public status, package count (run date kept).
- data/history/*.json: statuses mapped to the public statuses.
- data/changelog.json: status lines with public labels only (dropped when the public label did not change),
  counts by public status, neutral first-entry text.
Run: python3 scripts/migrate_public_data.py"""
import importlib.util, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("verify", os.path.join(ROOT, "scripts/verify.py"))
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)

def load(p): return json.load(open(os.path.join(ROOT, p)))
def dump(p, obj, indent=2): json.dump(obj, open(os.path.join(ROOT, p), "w"), indent=indent, ensure_ascii=False); open(os.path.join(ROOT, p), "a").write("\n") if indent == 2 else None

tools = load("data/tools.json")
rep_old = load("data/verification-report.json")
pub = [V.public_tool(t) for t in tools]
dump("data/tools.json", pub)
rep = V.public_report(pub); rep["checked_at"] = rep_old.get("checked_at", rep["checked_at"])
dump("data/verification-report.json", rep)

hd = os.path.join(ROOT, "data/history")
for f in sorted(os.listdir(hd)):
    if not f.endswith(".json"): continue
    snap = load(f"data/history/{f}")
    for s in snap.values(): s["status"] = V.to_public(s.get("status"))
    json.dump(snap, open(os.path.join(hd, f), "w"), indent=1)

log = load("data/changelog.json")
for w in log:
    w["counts"] = {}
    out = []
    for c in w["changes"]:
        if c.get("kind") == "launch":
            n = len(load(f"data/history/{w['date']}.json")) if os.path.exists(os.path.join(hd, f"{w['date']}.json")) else None
            out.append({"kind": "launch", "text": f"Directory published with {n} tools." if n else "Directory published."}); continue
        if c.get("kind") == "status":
            name, arrow = c["text"].rsplit(": ", 1)
            if "from" in c and "to" in c:          # already migrated
                a, b = c["from"], c["to"]
            else:
                a, b = (V.to_public(x.strip()) for x in arrow.split("→"))
            if a == b: continue
            out.append({"kind": "status", "id": c["id"], "from": a, "to": b, "text": f"{name}: {V.PUBLIC_LABEL[a]} → {V.PUBLIC_LABEL[b]}"}); continue
        out.append(c)
    w["changes"] = out
    hp = os.path.join(hd, f"{w['date']}.json")
    if os.path.exists(hp): w["counts"] = V.public_counts(load(f"data/history/{w['date']}.json"))
dump("data/changelog.json", log)
print("migrated", len(pub), "tools,", len(log), "changelog weeks")
