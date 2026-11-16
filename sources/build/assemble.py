import json, os, re, sys, math
sys.path.insert(0, '/home/claude/build')
import freq
from wordfreq import zipf_frequency
E = '/home/claude/en'
IT = json.load(open(f'{E}/it_data3d.json'))
ITR = {r['id']: r for r in IT['rooms']}
order = json.load(open(f'{E}/order.json'))
FAMN = {'noms': 'Nouns', 'verbes': 'Verbs', 'adjectifs': 'Adjectives', 'pronoms': 'Pronouns', 'conjonctions': 'Conjunctions',
        'prepositions': 'Prepositions', 'adverbes': 'Adverbs', 'courantes': 'Everyday expressions', 'modales': 'Modal expressions',
        'incises': 'Discourse markers', 'formes': 'Hall of mirrors', 'villes_pays': 'Cities and countries', 'patrons': 'Sentence patterns'}
DECOR = {'noms': 'halle de marché victorienne', 'verbes': "atelier d'ébéniste", 'adjectifs': 'galerie de peinture', 'pronoms': 'salon victorien',
         'conjonctions': 'salle des ponts de la Tamise', 'prepositions': "cour de collège d'Oxford", 'adverbes': 'théâtre du West End',
         'courantes': 'place de village anglais', 'modales': 'place de village anglais', 'incises': "Speakers' Corner",
         'formes': 'galerie des glaces : chaque forme reflète sa base', 'villes_pays': 'salle des cartes : globes et cartes de la Royal Geographical Society',
         'patrons': "bureau de l'architecte : plans et maquettes"}
ORD = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth',
       'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second',
       'twenty-third', 'twenty-fourth']
def base(rid): return re.sub(r'_\d+$', '', rid)
def load(p):
    try: return json.load(open(p))
    except Exception: return None
FORMES_IT = ['formes_1', 'formes_2', 'formes_3', 'formes_4']
TKIND = {'pluriel': ['noms'], 'comparatif': ['adjectifs'], 'superlatif': ['adjectifs'], 'ordinal': ['adjectifs'], 'pronom': ['pronoms'], 'possessif': ['pronoms']}
rooms = []; missing_rev = []
for rid in order:
    b = base(rid)
    meta = dict(ITR[rid]); itn = {}
    meta.pop('niches')
    fl = meta['floor']
    meta['it'] = FAMN[b] + (f' · {ORD[fl]} floor' if fl else '')
    meta['decor'] = DECOR[b] + (', étage' if fl else '')
    out = {y['n']: y for y in json.load(open(f'{E}/out/{rid}.json'))['niches']}
    rev = load(f'{E}/rev/{rid}.json') or {'fix': {}, 'li': {}}
    if not os.path.exists(f'{E}/rev/{rid}.json'): missing_rev.append(rid)
    fam = meta['fam']
    niches = [None] * 100
    if b == 'formes':
        src = {n: None for n in range(100)}
    else:
        src = dict(enumerate(ITR[rid]['niches']))
        if os.path.exists(f'{E}/{rid.split("_")[0]}_perm.json') and rid == 'villes_pays':
            perm = json.load(open(f'{E}/villes_perm.json'))
            src = {perm[str(k)]: v for k, v in enumerate(ITR[rid]['niches']) if str(k) in perm}
    for n in range(100):
        y = out.get(n)
        if not y or y.get('drop'): continue
        x = dict(src.get(n) or {})
        if b == 'formes':
            x = {'fr': y['fr'], 'efr': None, 'efm': None, 't': TKIND.get(y.get('kind'), ['verbes']), 'th': 'autres', 'scat': '', 'k': ''}
            inp = {z['n']: z for z in json.load(open(f'{E}/in/{rid}.json'))['niches']}[n]
            x['efr'] = inp['efr']; x['efm'] = inp['efm']
            zf = zipf_frequency(re.sub(r'\(.*?\)', '', y['fr']).strip(), 'fr')
            x['zf'] = round(zf, 2) or None; x['of'] = round(10 ** zf / 10) if zf else None; x['zfe'] = None
        for k in ('it', 'itd', 'ito', 'itp', 'pr', 'api', 'mc', 'sc', 'de', 'fo', 'eit', 'eim', 'cm', 'fr', 'frd'):
            if y.get(k) not in (None, ''): x[k] = y[k]
            elif k in ('itd', 'ito', 'itp') and k in x: x[k] = None
        if b == 'villes_pays':
            vin = {z['n']: z for z in json.load(open(f'{E}/in/{rid}.json'))['niches']}[n]
            y = dict(y); y.setdefault('fr', vin['fr']); y.setdefault('efr', vin['efr']); y.setdefault('efm', vin.get('efm'))
            x['fr'] = vin['fr']
        if b == 'villes_pays' and y.get('efr') and y['efr'] != x.get('efr'):
            x['efr'] = y['efr']; x['efm'] = y.get('efm') or x.get('efm')
            for k in ('ap', 'af', 'ai', 'ae'): x[k] = None
            zf = zipf_frequency(re.sub(r"^(l'|le |la |les )", '', y.get('fr') or x['fr']), 'fr')
            x['zf'] = round(zf, 2) or None; x['zfe'] = x['zf']; x['of'] = round(10 ** zf / 10) if zf else None
        for k, v in (rev.get('fix', {}).get(str(n)) or {}).items():
            if k in ('it', 'eit', 'eim', 'api', 'fr', 'frd', 'itd', 'pr'): x[k] = v
        x['li'] = (rev.get('li') or {}).get(str(n))
        if x.get('px'):
            pe = y.get('px') or []
            x['px'] = [[p[0], pe[i] if i < len(pe) else '', None, None] for i, p in enumerate(x['px'])]
        if y.get('co'):
            x['co'] = [[c, round(10 ** zipf_frequency(re.sub(r'\b(sb|sth)\b', '', c), 'en') / 10, 1), 0] for c in y['co']]
        else: x['co'] = None
        for k in ('am', 'ap', 'af', 'ai', 'ae'): x[k] = None
        zi, zie, oi, ax = freq.freq(x.get('ito') or x['it'], fam if fam in ('noms', 'verbes', 'adjectifs') else None)
        if x['it'].strip().lower() == 'nice': zi, zie, oi, ax = 3.18, 3.18, 150, True
        x['zi'], x['zie'], x['oi'], x['ax'] = zi, zie, oi, ax
        if x.get('tv') is not None: x['tv'] = float(oi or 0)
        if y.get('reuse') is not None: pass
        niches[n] = x
    meta['niches'] = niches
    rooms.append(meta)
# liens manquants + dernier lien de chaque pièce
flat = [(ri, n) for ri, r in enumerate(rooms) for n, x in enumerate(r['niches']) if x]
for i, (ri, n) in enumerate(flat):
    x = rooms[ri]['niches'][n]
    if i + 1 < len(flat):
        rj, m = flat[i + 1]; nx = rooms[rj]['niches'][m]
        if rj != ri:
            x['li'] = f"Avec {x['fr']}, on passe à la salle « {rooms[rj]['fr']} », où : {nx['sc']}"
        elif not x.get('li'):
            x['li'] = f"Après {x['fr']} vient la scène suivante : {nx['sc']}"
    else: x['li'] = None
# rangs par famille (fréquence parlée)
fams = {}
for r in rooms:
    for x in r['niches']:
        if x: fams.setdefault(r['fam'], []).append(x)
for L in fams.values():
    for k, x in enumerate(sorted(L, key=lambda x: -(x['oi'] or 0))): x['rk'] = k + 1
# courbe au-delà du palais (sous-titres anglais)
pal = set()
for r in rooms:
    for x in r['niches']:
        if x:
            for w in freq.clean(x['it']).split(): pal |= freq.forms(w, None) | {w}
rest = sorted((c for w, c in freq.SUB.items() if w not in pal), reverse=True)
tot = sum(rest); ext = []; acc = 0; nxt = 1
for k, c in enumerate(rest, 1):
    acc += c
    if k >= nxt or k == len(rest):
        ext.append([k, round(acc / tot, 5)]); nxt = max(k + 1, int(k * 1.09))
D = {'langue': 'anglais', 'rev': 1, 'migr': [], 'packs': [], 'ext': ext, 'themes': IT['themes'], 'scorder': IT['scorder'], 'rooms': rooms}
json.dump(D, open('/home/claude/build/data3d.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('pièces', len(rooms), 'niches', len(flat), 'ext', len(ext), 'sans relecture', missing_rev)
