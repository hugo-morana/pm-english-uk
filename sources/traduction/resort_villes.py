# retrie la salle villes_pays par fréquence anglaise (in/out/rev) et met à jour villes_perm.json (ancienne position italienne -> nouvelle)
import json, sys
sys.path.insert(0, '/home/claude/build'); import freq
i = json.load(open('in/villes_pays.json')); o = json.load(open('out/villes_pays.json')); rv = json.load(open('rev/villes_pays.json'))
perm = json.load(open('villes_perm.json')); inv = {v: k for k, v in perm.items()}
inp = {x['n']: x for x in i['niches']}
def it(y): return rv['fix'].get(str(y['n']), {}).get('it') or y['it']
def occ(y):
    if it(y).strip().lower() == 'nice': return 150
    return freq.freq(it(y))[2] or 0
ys = sorted(o['niches'], key=lambda y: -occ(y))
newperm = {}; ni = []; no = []; nf = {}
for k, y in enumerate(ys):
    if y['n'] in inv: newperm[inv[y['n']]] = k
    x = dict(inp[y['n']]); x['n'] = k; ni.append(x)
    y2 = dict(y); y2['n'] = k; no.append(y2)
    if str(y['n']) in rv['fix']: nf[str(k)] = rv['fix'][str(y['n'])]
i['niches'] = ni; o['niches'] = no
json.dump(i, open('in/villes_pays.json', 'w'), ensure_ascii=False); json.dump(o, open('out/villes_pays.json', 'w'), ensure_ascii=False)
json.dump({'fix': nf, 'li': {}}, open('rev/villes_pays.json', 'w'), ensure_ascii=False)
json.dump(newperm, open('villes_perm.json', 'w'))
print([(it(y), occ(y)) for y in ys])
