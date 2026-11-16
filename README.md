# pm-english-uk — Palace of English

Palais mental 3D de vocabulaire d'**anglais britannique** pour francophones, réplique du [Palazzo dell'italiano](https://github.com/hugo-morana/pm-italien).

- 92 salles, 8 166 niches, rangées comme le palais italien (fréquence du mot français à l'oral) ; mêmes phrases d'exemple françaises.
- Traduction en anglais britannique natif, relue par des relecteurs indépendants ; API en anglais britannique standard (SSBE) ; mot-clé sonore français, scène mnémotechnique à touche britannique, liens de chaîne.
- Salles des formes : formes anglaises à apprendre (verbes irréguliers, be / have / do, modaux, contractions, pluriels irréguliers, comparatifs, pronoms, ordinaux), triées par fréquence anglaise.
- Salle Villes et pays triée par fréquence anglaise, villes italiennes remplacées par des villes britanniques et irlandaises.
- Fréquences anglaises : OpenSubtitles 2018 (oral) et wordfreq (écrit, expressions).
- Sons : voix française Hugo Pro reprise du palais italien (`audio/fr_<salle>.mp3`) ; anglais en voix britannique de l'appareil en attendant les sons ElevenLabs.
- Progression : appareil, ou compte e-mail Supabase (`config.js`, `supabase/schema.sql`) ; les clés sont préfixées `en:` pour ne pas se mélanger avec le palais italien si le même projet Supabase sert aux deux.

## Fabrication
- `sources/traduction/` : consignes (`SPEC.md`, `FORMES_SPEC.md`, `REVIEW_SPEC.md`), entrées par salle (`in/`), traductions (`out/`), relectures et liens (`rev/`), salles des formes (`formes/`).
- `sources/build/` : `patch_index.py` (adaptation de la page italienne), `assemble.py` (data3d.json), `freq.py` (fréquences), `fraudio.py` (paquets de sons français).
