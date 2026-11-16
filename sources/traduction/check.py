import json, sys, re
rid = sys.argv[1]
inp = json.load(open(f"/home/claude/en/in/{rid}.json"))["niches"]
out = json.load(open(f"/home/claude/en/out/{rid}.json"))["niches"]
errs = []
on = {x["n"]: x for x in out}
for x in inp:
    n = x["n"]; y = on.get(n)
    if not y: errs.append(f"{n}: manquante"); continue
    if y.get("drop"): continue
    for k in ("it", "eit", "eim", "api", "pr", "mc", "sc", "de"):
        if not y.get(k): errs.append(f"{n}: champ {k} vide")
    if "fo" not in y: errs.append(f"{n}: champ fo absent")
    for k in ("itd", "ito", "itp", "cm"):
        if x.get(k) and not y.get(k): errs.append(f"{n}: champ {k} attendu")
    if x.get("px") and len(y.get("px") or []) != len(x["px"]): errs.append(f"{n}: px doit avoir {len(x['px'])} phrases")
    e = (y.get("eit") or "").lower(); at = 0
    for seg in (y.get("eim") or "").split("|"):
        if not seg: continue
        k = e.find(seg.lower(), at)
        if k < 0: errs.append(f"{n}: eim « {seg} » introuvable dans eit dans l'ordre"); break
        at = k + len(seg)
    a = y.get("api") or ""
    if a and not (a.startswith("/") and a.endswith("/")): errs.append(f"{n}: api sans barres obliques")
    if re.search(r"\b(gotten|apartment|vacation|cellphone|sidewalk|color|favor|center|realize)\b", e): errs.append(f"{n}: américanisme possible dans eit : {y['eit']}")
extra = set(on) - {x["n"] for x in inp}
if extra: errs.append(f"niches en trop : {sorted(extra)}")
print("\n".join(errs[:60]) if errs else "OK")
