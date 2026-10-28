# Nico Shield

Landing page e-commerce une page (`index.html` + `assets/`) qui vend la gamme Nicorette® au Maroc :
paiement à la livraison (COD), commande envoyée sur WhatsApp, public adulte 18+.
Pas de build : HTML/CSS/JS statique, GSAP via cdnjs. Tester avec `python3 -m http.server 8080`.
Aperçu artifact (https://claude.ai/artifact/7qaKr4LRSiThENTokwnSs3) : il ne charge pas les fichiers
`assets/` séparés, donc lancer `python3 scripts/build-artifact.py` et publier `deploy/artifact.html`
(images intégrées en data URI) sur cette URL. Dans `index.html`, écrire les chemins d'images en entier
(`assets/xxx.webp`) pour que le script les trouve.

## Contexte métier
- Produit unique : Nicorette® gomme 4 mg **Menthe fraîche**, boîte de 105 (7 plaquettes de 15).
  Prix : 1 boîte 500 DH, 2 boîtes 900 DH, 4 boîtes (3 + 1 offerte) 1 500 DH ; livraison toujours offerte.
- Posologie affichée = celle de la notice : 8 à 12 gommes/jour au début, puis réduction, 15 max/jour.
- Marché marocain : COD dominant, confirmation WhatsApp, prix en DH, villes listées dans le formulaire.
- Langue du site : français, avec touches de darija (script arabe) ; l'utilisateur écrit en français.
- Produits = médicaments (nicotine) : rester factuel, pas d'allégation de guérison, garder posologie,
  précautions, porte d'âge et mentions légales. Pubs Meta/TikTok restreintes pour la nicotine.

## Skills : charger automatiquement, sans attendre qu'on le demande
À chaque message, identifier le ou les skills de `.claude/skills/` qui couvrent la demande,
les lire (SKILL.md puis les `references/` utiles) et les appliquer. Plusieurs skills peuvent se combiner.

| Demande | Skills |
|---|---|
| Conversion, page de vente, formulaire COD | `cro`, `marketing-psychology`, `offers`, `pricing`, `ab-testing`, `popups` |
| Textes, titres, accroches | `copywriting`, `copy-editing`, `product-marketing` |
| Pubs Meta/TikTok, créas, UGC | `ads`, `ad-creative`, `image`, `video`, `influencer-marketing`, `social` |
| WhatsApp / SMS / emails, relances | `sms`, `emails`, `churn-prevention`, `referrals` |
| SEO, schema, IA search | `seo-audit`, `schema`, `ai-seo`, `site-architecture`, `programmatic-seo` |
| Stratégie, lancement, concurrence | `marketing-plan`, `launch`, `competitors`, `competitor-profiling`, `customer-research`, `marketing-ideas`, `marketing-council` |
| Tracking, Pixel, analytics | `analytics`, `attribution` |
| Design, direction artistique, refonte | `impeccable`, `design-taste-frontend` (taste-skill), `high-end-visual-design`, `redesign-existing-projects`, `design-dna`, `ckm:design`, `ckm:ui-styling`, `ui-ux-pro-max` |
| Marque, bannières | `ckm:brand`, `brandkit`, `ckm:banner-design` |
| Animation, micro-interactions | `cast` + `paint` (genjutsu, sous-skills dans `_jutsu/`), `motion-design`, `gsap-*` |
| Scroll storytelling | `scroll-world`, `gsap-scrolltrigger` |
| 3D (boîte produit, scènes) | `threejs-*` |
| Vidéo promo animée | `motion-design-video`, `saas-motion-video` |

Les scripts fournis par certains skills (impeccable, ui-ux-pro-max, motion-design-video…) ne sont lancés
que si le skill l'exige pour la tâche en cours ; ne jamais activer leurs hooks ni envoyer de données
à un service externe sans l'accord de l'utilisateur.
