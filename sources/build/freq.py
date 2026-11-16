import math, re
from wordfreq import zipf_frequency
from lemminflect import getAllInflections
SUB = {}; TOT = 0
for line in open('/tmp/en_full.txt', encoding='utf-8'):
    w, c = line.rsplit(' ', 1); c = int(c); SUB[w] = SUB.get(w, 0) + c; TOT += c
def clean(s):
    s = str(s or '').split(' / ')[0]
    s = re.sub(r'\(.*?\)|\[.*?\]', ' ', s)
    s = re.sub(r'\b(sb|sth|somewhere|S|V|C)\d?\b', ' ', s)
    s = re.sub(r"[^A-Za-z' -]", ' ', s).strip().lower()
    s = re.sub(r'^to ', '', s)
    return re.sub(r'\s+', ' ', s).strip()
def occ_word(w):  # occurrences /100 M in subtitles
    return SUB.get(w, 0) / TOT * 1e8
def forms(w, pos):
    out = {w}
    try:
        for k, v in getAllInflections(w, upos=pos).items(): out.update(v)
    except Exception: pass
    return out
def freq(item, fam=None, lemma=True):
    """renvoie (zi parlé, zie écrit, oi occ/100M parlé, approx)"""
    s = clean(item)
    if not s: return None, None, None, True
    if ' ' not in s:
        pos = {'verbes': 'VERB', 'noms': 'NOUN', 'adjectifs': 'ADJ'}.get(fam)
        fs = forms(s, pos) if (lemma and pos) else {s}
        o = sum(occ_word(f) for f in fs)
        zw = zipf_frequency(s, 'en')
        if o > 0:
            return round(math.log10(o * 10), 2), round(zw, 2), round(o), False
        return round(zw, 2), round(zw, 2), round(10 ** zw / 10), True
    zw = zipf_frequency(s, 'en')
    return round(zw, 2), round(zw, 2), round(10 ** zw / 10) if zw else 0, True
