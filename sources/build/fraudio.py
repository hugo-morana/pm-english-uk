import json, os, hashlib, subprocess
IT = json.load(open('/home/claude/en/it_data3d.json'))
P = IT['packs']; AUD = '/tmp/pm-italien/audio'
FRW, FRS = {}, {}
for r in IT['rooms']:
    for x in r['niches']:
        if not x: continue
        if x.get('af'): FRW.setdefault(x['fr'], x['af'])
        if x.get('ae'): FRS.setdefault(x['efr'], x['ae'])
        for p in x.get('px') or []:
            if len(p) > 2 and p[2]: FRS.setdefault(p[0], p[2])
D = json.load(open('data3d.json'))
cache = {}
def raw(ref):
    i, off, ln = ref
    if i not in cache: cache[i] = open(os.path.join(AUD, P[i].split('?')[0].split('/', 1)[1]), 'rb').read()
    return cache[i][off:off + ln]
os.makedirs('site/audio', exist_ok=True)
packs = []; nw = ns = npx = 0; tot = 0
for r in D['rooms']:
    buf = bytearray(); seen = {}
    def put(ref):
        global tot
        k = tuple(ref)
        if k in seen: return seen[k]
        b = raw(ref); off = len(buf); buf.extend(b); seen[k] = [len(packs), off, len(b)]; return seen[k]
    for x in r['niches']:
        if not x: continue
        a = FRW.get(x['fr']); e = FRS.get(x.get('efr'))
        x['af'] = put(a) if a else None; x['ae'] = put(e) if e else None
        nw += bool(a); ns += bool(e)
        for p in x.get('px') or []:
            c = FRS.get(p[0]); p[2] = put(c) if c else None; npx += bool(c)
    if buf:
        name = f"audio/fr_{r['id']}.mp3"
        open('site/' + name, 'wb').write(buf)
        packs.append(name + '?v=' + hashlib.sha1(buf).hexdigest()[:8]); tot += len(buf)
    else:
        # aucune référence : retirer les index réservés
        pass
D['packs'] = packs
json.dump(D, open('site/data3d.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('mots', nw, 'phrases', ns, 'px', npx, 'paquets', len(packs), 'Mo', round(tot / 1e6, 1))
