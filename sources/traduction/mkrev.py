import json, sys, os
for rid in sys.argv[1:]:
    inp = {x['n']: x for x in json.load(open(f'in/{rid}.json'))['niches']}
    out = json.load(open(f'out/{rid}.json'))['niches']
    L = []
    for y in sorted(out, key=lambda y: y['n']):
        if y.get('drop'): continue
        x = inp[y['n']]
        L.append({'n': y['n'], 'fr': y.get('fr') or x['fr'], 'efr': x.get('efr'), 'it': y['it'], 'eit': y['eit'], 'eim': y['eim'], 'api': y['api'], 'sc': y['sc']})
    json.dump(L, open(f'revin/{rid}.json', 'w'), ensure_ascii=False, indent=0)
    print(rid, len(L), os.path.getsize(f'revin/{rid}.json'))
