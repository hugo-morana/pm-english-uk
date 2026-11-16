import re, sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src).read()
def rep(old, new, count=None, must=True):
    global t
    n = t.count(old)
    if must and n == 0: raise SystemExit("introuvable: " + old[:80])
    if count is not None and n != count: raise SystemExit(f"{n} occurrences (attendu {count}): {old[:80]}")
    t = t.replace(old, new)
# titres
rep("Palazzo dell'italiano", "Palace of English")
rep('localStorage.getItem("pmit:"', 'localStorage.getItem("pmen:"', 1)
rep('localStorage.setItem("pmit:"', 'localStorage.setItem("pmen:"', 1)
# normalisation : articles anglais
rep(r'.replace(/\b(il|lo|la|i|gli|le|l|un|una|uno|le|les|de|du|des)\b/g, " ")', r'.replace(/\b(the|a|an|to|le|la|les|l|un|une|de|du|des)\b/g, " ")', 1)
# voix
rep('vs = all.filter(v => /^it/i.test(v.lang))', 'vs = all.filter(v => /^en/i.test(v.lang))', 1)
rep('voice = vs.find(v => /it-IT/i.test(v.lang) && v.localService) || vs[0] || null', 'voice = vs.find(v => /en-GB/i.test(v.lang) && v.localService) || vs.find(v => /en-GB/i.test(v.lang)) || vs[0] || null', 1)
rep('"it-IT"', '"en-GB"')
rep('lang="it-fonipa"', 'lang="en-GB-fonipa"')
rep('lang="it"', 'lang="en-GB"')
rep("Aucune voix italienne sur cet appareil", "Aucune voix anglaise sur cet appareil")
# trous sb / sth
rep(r'/\bda qlc parte\b/g, lang === "fr" ? "quelque part" : "da qualche parte"', r'/\bsomewhere\b/g, lang === "fr" ? "quelque part" : "somewhere"', 1)
rep(r"/\bqcn\b/g, lang === " + '"fr" ? "quelqu' + "'" + 'un" : "qualcuno"', r"/\bsb\b/g, lang === " + '"fr" ? "quelqu' + "'" + 'un" : "somebody"', 1)
rep(r'/\bqcs\b/g, lang === "fr" ? "quelque chose" : "qualcosa"', r'/\bsth\b/g, lang === "fr" ? "quelque chose" : "something"', 1)
rep("qn / qcn = quelqu'un (qualcuno), qc / qcs = quelque chose (qualcosa), qqpart = quelque part (da qualche parte)", "qn / sb = quelqu'un (somebody), qc / sth = quelque chose (something), qqpart = quelque part (somewhere)", 1)
# mots de la phrase : jeux de mots anglais
rep('''.replace(/'/g, "' ").replace(/[^a-zà-öø-ÿ' ]/g, " ")''', '''.replace(/[^a-zà-öø-ÿ' ]/g, " ")''', 1)
rep('''.replace(/'/g, "' ").replace(/[^A-Za-zÀ-ÖØ-öø-ÿ0-9' ]/g, " ")''', '''.replace(/[^A-Za-zÀ-ÖØ-öø-ÿ0-9' ]/g, " ")''', 1)
rep(r"/^(il|lo|la|i|gli|le|l'|un|una|uno|un')$/.test(t[0])", r"/^(the|a|an|to)$/.test(t[0])", 1)
t = re.sub(r"const AUXW = new Set\(`.*?`\.split\(/\\s\+/\)\);", lambda m: "const AUXW = new Set(`have has had 've 's 'd having am is are was were be been being 'm 're do does did will would shall should can could may might must`.split(/\\s+/));", t, count=1, flags=re.S)
t = re.sub(r'const SKIPW = new Set\(".*?"\.split\(" "\)\);', 'const SKIPW = new Set("not never just already always also still really only ever even often n\'t".split(" "));', t, count=1)
t = re.sub(r"const DETW = new Set\(`.*?`\.split\(/\\s\+/\)\);", lambda m: "const DETW = new Set(`the a an this that these those my your his her its our their every some any no each another`.split(/\\s+/));", t, count=1, flags=re.S)
rep('const PREPW = new Set("a ad in da per con su fino tra fra".split(" "));', 'const PREPW = new Set("in at to from with on for by into about between".split(" "));', 1)
rep('const TONW = new Set("me te lui lei noi voi loro sé".split(" "));', 'const TONW = new Set("me him her us them you".split(" "));', 1)
rep('const MOISW = new Set("gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split(" "));', 'const MOISW = new Set("january february march april may june july august september october november december".split(" "));', 1)
t = re.sub(r"const NUMW = /\^\(\\d\+\|due\|.*?\)\$/;", r"const NUMW = /^(\\d+|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)$/;", t, count=1)
rep("const lead = T.length > 1 && /o$/.test(T[0].w)", "const lead = false && T.length > 1 && /o$/.test(T[0].w)", 1)
rep("`Dal ${lo} al ${hi} % di ${kind === \"freq\" ? \"espressione\" : \"comprensione\"}`", "`From ${lo} to ${hi} % of ${kind === \"freq\" ? \"speaking\" : \"understanding\"}`", 1)
# textes visibles
for a, b in [("Phrase IT → FR", "Phrase EN → FR"), ("Phrase FR → IT", "Phrase FR → EN"), ("FR → IT", "FR → EN"), ("IT → FR", "EN → FR"),
             ("Par fréquence IT", "Par fréquence EN"), ("Fréquence IT", "Fréquence EN"), ("fréq. IT", "fréq. EN"), ("fréquence IT", "fréquence EN"),
             ("Mot IT", "Mot EN"), ("Exemple IT", "Exemple EN"), ("Compréhension IT", "Compréhension EN"),
             ("Traduis en italien", "Traduis en anglais"), ("que l'italien préfère", "que l'anglais préfère")]:
    t = t.replace(a, b)
t = t.replace("l'italien", "l'anglais").replace("L'italien", "L'anglais").replace("italienne", "anglaise").replace("Italienne", "Anglaise")
t = re.sub(r"(?<![\w-])italien(?!\w)", "anglais", t)
t = t.replace("dell'anglais", "de l'anglais")
open(dst, "w").write(t)
left = [m.start() for m in re.finditer(r"\bIT\b|italien|Italien|qcn|qcs|qualc", t)]
print("reste:", len(left))
for p in left[:20]: print(repr(t[p-60:p+40]))

# --- ambiance britannique ---
t = open(dst).read()
import homes_en
t = homes_en.apply(t)
a = t.index("const FAMS = {"); b = t.index("};", a) + 2
t = t[:a] + '''const FAMS = {
  noms:         { fr: "halle de marché victorienne", it: "market hall", floor: ["carreaux", "#8c2f2a", "#e8dcc6"], wall: "#e6d8bf", ceil: "#eee4d2", land: "etal" },
  verbes:       { fr: "atelier d'ébéniste", it: "joiner's workshop", floor: ["parquet", "#6b4a2e", "#8a6440"], wall: "#d6cab4", ceil: "#e6dcc8", land: "etabli" },
  adjectifs:    { fr: "galerie de peinture", it: "picture gallery", floor: ["marbre", "#ece7de", "#8f8a82"], wall: "#2f4a3a", ceil: "#efe9de", land: "chevalet" },
  pronoms:      { fr: "salon victorien", it: "drawing room", floor: ["tapis", "#24345a", "#c9a24a"], wall: "#e8dfcf", ceil: "#f2ece0", land: "fauteuil" },
  conjonctions: { fr: "salle des ponts de la Tamise", it: "bridge room", floor: ["damier", "#1f3550", "#d8d4cc"], wall: "#c5cdd3", ceil: "#e3e6e8", land: "pont" },
  prepositions: { fr: "cour de collège d'Oxford", it: "college quad", floor: ["gazon", "#4f7a3a", "#3e6430"], wall: "#d6c7a3", ceil: "#93a8bd", land: "colonne" },
  adverbes:     { fr: "théâtre du West End", it: "West End theatre", floor: ["planches", "#5b3a26", "#714a30"], wall: "#6e1a22", ceil: "#22191f", land: "rideau" },
  expressions:  { fr: "place de village anglais", it: "village green", floor: ["pierre", "#9a978f", "#6f6c66"], wall: "#c9b28a", ceil: "#9fb4c7", land: "fontaine" },
  incises:      { fr: "Speakers' Corner", it: "Speakers' Corner", floor: ["gazon", "#5d8a45", "#46703a"], wall: "#d9d0bf", ceil: "#a9bccb", land: "lutrin" },
  accords:      { fr: "salle des reflets", it: "hall of reflections", floor: ["marbre", "#e6dccb", "#8a7a64"], wall: "#3b4a6b", ceil: "#ece6dc", land: "chevalet" },
  formes:       { fr: "galerie des glaces", it: "hall of mirrors", floor: ["marbre", "#d8d4cc", "#6f6a62"], wall: "#24405a", ceil: "#e8e4dc", land: "etabli" },
  patrons:      { fr: "bureau de l'architecte", it: "architect's office", floor: ["damier", "#26394a", "#e3dccb"], wall: "#c9d4d8", ceil: "#eef0ec", land: "lutrin" }
};''' + t[b:]
# accent : rouge boîte aux lettres / bleu marine
t = t.replace("--accent:#9c3d22", "--accent:#a3202b").replace("--hl:#f1d3bd", "--hl:#f3cfd2")
open(dst, "w").write(t)
print("ambiance ok")
