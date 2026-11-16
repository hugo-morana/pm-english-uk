# Palais d'anglais britannique — phase B : relecture native + liens de chaîne

Tu es relecteur, anglais britannique natif (Londres / sud de l'Angleterre), bilingue français. Une autre personne a traduit cette pièce ; tu ne l'as pas écrite, ton rôle est de la corriger sans complaisance.

Entrée : `/home/claude/en/revin/<id>.json` — liste de niches dans l'ordre de visite, avec `n`, `fr` (item français), `efr` (phrase française, INTOUCHABLE), `it` (traduction anglaise de l'item), `eit` (phrase anglaise), `eim` (partie surlignée de `eit`, segments séparés par « | »), `api`, `sc` (scène mnémotechnique en français).

## 1. Relecture (uniquement ce qui est faux ou pas naturel)
- `eit` doit être ce qu'un Britannique natif dirait vraiment dans la même situation et le même registre que `efr` : naturel, idiomatique, orthographe et vocabulaire britanniques (flat, mobile, queue, holiday, rubbish, mum, colour…), pas d'américanismes (gotten, apartment, vacation, I'm good…), pas de calque du français, contractions de l'oral. Le sens doit être fidèle à `efr`.
- `it` doit correspondre au sens de l'item dans la phrase et apparaître dans `eit` ; `eim` doit surligner exactement ce mot (sous-chaînes exactes de `eit`).
- `api` : SSBE / RP moderne, non rhotique (/ˈwɔːtə/, /kɑːnt/, /bɑːθ/), entre barres obliques.
- `fr` : s'il cite un mot italien entre parenthèses (« (cosa, pluriel) »), réécris-le avec le mot anglais : « (thing, pluriel) ».
Ne touche pas à ce qui est correct. Si tu changes `it`, vérifie que `eit`/`eim` restent cohérents (et inversement).

## 2. Liens de chaîne `li`
Pour chaque niche sauf la dernière de la liste, écris `li` : UNE phrase française vive (25 mots maximum) qui fait passer physiquement de l'image de sa scène `sc` à l'image de la scène de la niche suivante (un objet tombe, roule, s'envole, quelqu'un tend, pousse, lance… vers l'élément clé de la scène suivante). Réutilise les éléments en MAJUSCULES des deux scènes. Pas de « puis vient la scène suivante ».

## Sortie
`/home/claude/en/rev/<id>.json` = `{"fix": {"<n>": {"<champ>": "<nouvelle valeur>", ...}, ...}, "li": {"<n>": "...", ...}}` (clés `n` en chaînes). Écris par lots dans `/home/claude/en/rev/<id>.partial.json` pour ne rien perdre, et reprends-le s'il existe déjà. Vérifie avec Python que chaque segment de `eim` (corrigé ou non) est une sous-chaîne de `eit` (corrigé ou non) et que toutes les niches sauf la dernière ont un `li`.
Réponds en une ligne : « <id> : <nombre> corrections, <nombre> liens ».
