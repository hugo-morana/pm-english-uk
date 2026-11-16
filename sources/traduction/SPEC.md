# Palais mental 3D — version ANGLAIS BRITANNIQUE (phase A : traduction d'une pièce)

Tu adaptes une pièce du « Palazzo dell'italiano » (palais mental de vocabulaire pour un francophone) en palais d'**anglais britannique**. Entrée : `/home/claude/en/in/<id>.json`. Sortie : `/home/claude/en/out/<id>.json`.

Chaque niche d'entrée contient : `n` (place 0-99), `fr` (mot / expression français), parfois `frd`/`fro`/`frp` (affichage / tournure / patron FR), `efr` (phrase d'exemple française) et `efm` (partie surlignée), et la version italienne (`it`, `itd`, `ito`, `itp`, `eit`, `eim`, `fo`, `mc`, `sc`, `de`, `px`, `co`, `cm`) qui sert de **modèle de structure** et de source pour l'image du sens français.

## Règle d'or
**La phrase française `efr` ne change jamais.** Tu la traduis directement depuis le français (pas depuis l'italien) en anglais britannique naturel, tel qu'un Anglais natif (sud de l'Angleterre / Londres, anglais standard) le dirait vraiment à l'oral, **dans le même registre** (familier → familier : « T'as le temps ? » → "Got a sec?" ou "Have you got time?" ; neutre → neutre). Pas de calque du français, pas d'américanismes.
- Orthographe britannique : colour, realise, centre, travelling, programme, grey, mum, cheque, tyre, practise (verbe)…
- Vocabulaire britannique : flat, lift, queue, mobile, holiday, autumn, rubbish, pavement, motorway, petrol, trousers, biscuit, chips/crisps, post, film, shop, timetable, term, maths, toilet/loo, quid…
- Grammaire britannique : "have got" quand c'est naturel, "gotten" interdit, present perfect là où un Britannique l'emploie ("I've just eaten", pas "I just ate"), contractions naturelles à l'oral (I'm, don't, it's, we'll), question tags si le français a « hein ? / non ? » ("isn't it?"), "at the weekend", "in hospital", "different from/to".
- Les noms propres et villes restent (Rome, Paris, Marie) ; € peut devenir £ si la phrase parle d'argent du quotidien, sinon garde.

## Champs de sortie par niche (les noms de champs `it*` contiennent désormais l'ANGLAIS)
- `n` : comme l'entrée.
- `it` : la meilleure traduction anglaise de l'item **dans le sens où il est employé dans `efr`**. Noms sans article ("thing", "man") sauf si l'article fait partie de l'expression ; verbes à l'infinitif avec to ("to be", "to get on with sb") ; adjectifs, adverbes etc. nus. Si l'item français a deux traductions également naturelles, mets la plus fréquente à l'oral britannique ; tu peux ajouter une variante après " / " seulement si elle est vraiment courante.
- **Cohérence obligatoire** : l'item `it` doit apparaître (ou sa forme fléchie) dans ta phrase `eit`. Si la traduction naturelle de la phrase n'emploie pas ton premier choix, c'est la phrase qui commande : choisis comme `it` le mot que la phrase naturelle emploie (s'il traduit bien l'item français).
- `itd` (seulement si l'entrée a `itd`) : affichage à trous, comme l'italien, avec [n] [v] [adj] [sb] [sth] [qty]… Ex. « Que [v] [qn] ? » → "What [v] [sb]?".
- `ito` (seulement si l'entrée a `ito`) : la tournure codée (S V C…) dans l'ordre des mots anglais. Ex. "Che cosa V S?" → "What do S V?".
- Tournures à trous (`k` = "tpl") : `it` s'écrit avec **sb** (somebody), **sth** (something), **somewhere** à la place de qcn / qcs / da qlc parte. Ex. « Que fait qn ? » → "What does sb do?".
- `itp` (patrons seulement) : le patron anglais ([S] [V] [COD]…), et `cm` : commentaire en français sur la structure anglaise (adapte celui de l'italien).
- `eit` : la phrase `efr` en anglais britannique natif (voir Règle d'or).
- `eim` : la ou les parties exactes de `eit` à surligner (le mot étudié et ses compléments comme `efm` en français), séparées par « | » dans l'ordre d'apparition ; chaque segment doit être une sous-chaîne exacte de `eit` (casse indifférente).
- `api` : transcription API en anglais britannique standard moderne (SSBE / RP), entre barres obliques, avec l'accent ˈ (et ˌ si utile) : "thing" → /θɪŋ/, "water" → /ˈwɔːtə/ (non rhotique !), "can't" → /kɑːnt/, "bath" → /bɑːθ/. Pour une expression, transcris l'expression (sans sb/sth).
- `pr` : prononciation figurée pour un francophone, syllabe accentuée en MAJUSCULES, syllabes séparées par des tirets ; `th` = son th, `h` = h soufflé, `e` = schwa. Ex. "water" → "OUO-te", "thing" → "THING", "comfortable" → "KAMF-te-bel".
- `mc` : mot-clé sonore FRANÇAIS qui ressemble au son du mot anglais (méthode phono-sémantique, comme l'italien : cosa → « Cosaque »). Ex. thing → « singe », water → « ouate ».
- `sc` : UNE scène mnémotechnique en français (1 à 2 phrases vives et concrètes) qui fusionne : (1) **l'image du mot français**, que tu reprends telle quelle de la scène / du décryptage italiens (elle est identique dans tous les palais : pour « chose », le paquet mystérieux marqué « ? ») ; (2) l'image du mot-clé sonore anglais ; (3) une **ambiance britannique** (bus rouge à impériale, cabine téléphonique rouge, black cab, thé de 17 h, pluie fine, pub, Big Ben, garde à bonnet en poil d'ours, fish and chips, Union Jack, cottage, Tamise…) — varie, n'en abuse pas, une touche suffit. Mets en MAJUSCULES le mot-clé sonore et le mot français, comme l'italien.
- `de` : décryptage court : "thing ≈ singe ; le paquet « ? » = une chose".
- `fo` : note de forme / usage en français pour l'anglais : pluriel irrégulier, formes du verbe (prétérit, participe : "went, gone"), indénombrable, faux ami, nuance UK/US si utile ("UK flat / US apartment"). Court. Chaîne vide si rien d'utile.
- `px` (seulement si l'entrée a `px`) : liste des traductions britanniques des phrases françaises de `px` (le 1er élément de chaque paire), dans le même ordre (liste de chaînes).
- `co` (seulement si l'entrée a `co`) : 2 à 4 collocations anglaises britanniques fréquentes du mot (chaînes).
- `fr` / `frd` : à ne fournir que si l'étiquette française porte une précision propre à l'italien qui n'a pas de sens pour l'anglais (ex. « le (devant consonne) » → « le, la, les (article défini) »). Sinon n'écris pas ces champs.
- `drop` : `true` si la niche n'existe que pour une distinction italienne et ferait, en anglais, doublon exact (même réponse anglaise, même sens) avec une niche précédente de la pièce (ex. il / lo / l' → tous "the" : garde la première, `drop` les autres). Une niche `drop` ne contient que `n` et `drop`. Sois parcimonieux : un sens différent n'est jamais un doublon.


## Points de vigilance (relevés sur la première pièce)
- Étiquettes françaises qui citent un mot italien entre parenthèses (« les choses (cosa, pluriel) », « été (essere / stare, participe) ») : fournis toujours `fr` (et `frd` si présent) réécrit avec la base anglaise : « les choses (thing, pluriel) ».
- Même pour une forme dérivée (pluriel, forme accordée…), `sc` est une vraie scène visuelle, jamais une explication grammaticale.
- Ordre des mots naturel en anglais : « Le matin, je bois un café » → "I have a coffee in the morning", pas "In the mornings, I have a coffee". « de la soirée » → "of the night" / "all night" selon l'usage.

## Méthode
0. Si `/home/claude/en/out/<id>.partial.json` existe déjà (travail interrompu), reprends-le et ne traite que les niches manquantes.
1. Lis l'entrée avec Python. Traite les niches par lots d'environ 25 ; après chaque lot, ajoute-les à `/home/claude/en/out/<id>.partial.json` (liste JSON) avec un petit script Python (`json.dump(..., ensure_ascii=False)`), pour ne jamais tout perdre.
2. Quand tout est fait, écris `/home/claude/en/out/<id>.json` = `{"niches": [...]}` (toutes les niches de l'entrée, dans l'ordre), puis lance `python3 /home/claude/en/check.py <id>` et corrige jusqu'à « OK ».
3. Relis-toi : chaque `eit` doit sonner comme un Anglais, pas comme une traduction.
4. Réponds en une seule ligne : « <id> OK, <nombre> niches, <nombre> drop ». Pas de résumé.
