# Palais anglais britannique — salles des FORMES (miroirs)

Dans le palais italien, les « salles des miroirs » contiennent les formes fléchies utiles (participes, formes accordées…), chacune avec sa phrase d'exemple. Pour l'anglais, on remplace ces salles par les **formes anglaises qu'un francophone doit apprendre séparément** : celles qu'on ne peut pas déduire de la forme de base.

Lis d'abord `/home/claude/en/SPEC.md` (règles d'anglais britannique natif, définitions des champs `it`, `eit`, `eim`, `api`, `pr`, `mc`, `sc`, `de`, `fo`). Les mêmes règles s'appliquent ici.

## Ta part
Elle est donnée dans ton message (ex. verbes irréguliers de a à g). Produis une niche par forme distincte :
- verbes irréguliers : le prétérit et le participe passé, **chacun sa niche** quand ils diffèrent ; une seule niche « prétérit et participe » quand ils sont identiques ("said", "made") ; aucune niche si la forme est identique à la base et se prononce pareil ("put", "cut") ; une niche si l'orthographe est identique mais la prononciation change ("read" /red/). Variantes britanniques courantes ("learnt", "burnt", "dreamt", "spelt") : forme britannique en premier, variante après " / ". Prends les verbes irréguliers vraiment courants à l'oral (ignore les archaïques : smite, slay…).
- autres parts : voir ton message.

## Phrases d'exemple françaises
Réutilise **en priorité une phrase française existante du palais** qui, traduite naturellement en anglais, emploie cette forme : cherche dans `/home/claude/en/formes/pool_formes_it.json` (phrases des salles des formes italiennes) puis dans `/home/claude/en/formes/phrases_fr_palais.txt` (toutes les phrases du palais), par exemple avec grep. Indique `"reuse": true` si la phrase vient de là. Sinon écris une phrase française orale naturelle, courte, et `"reuse": false`. Chaque phrase est employée une seule fois dans ta part.

## Champs par niche
`fr` (étiquette française, modèle : « allé (go, prétérit) », « été (be, participe) », « les hommes (man, pluriel) », « meilleur (good, comparatif) », « je suis (I am, forme contractée) »), `it` (la forme anglaise), `base` (la forme de base anglaise : "go"), `kind` ("preterit", "participe", "preterit_participe", "pluriel", "comparatif", "superlatif", "contraction", "auxiliaire", "modal"), `efr`, `efm`, `eit`, `eim`, `api`, `pr`, `mc` (mot-clé sonore français, avec le rappel de la base comme l'italien : « went → ouin ! (→ go) »), `sc` (scène qui relie la forme à sa base, avec l'image du sens français et une touche britannique), `de`, `fo` (ex. "go, went, gone"), `reuse`.

## Méthode
Écris par lots dans `/home/claude/en/formes/<part>.partial.json`, puis le résultat final `/home/claude/en/formes/<part>.json` = `{"niches": [...]}`, triées de la plus fréquente à l'oral à la plus rare (à ton estimation). Vérifie avec Python que chaque segment de `eim` est une sous-chaîne de `eit`. Réponds en une ligne : « <part> OK, <nombre> niches ».
