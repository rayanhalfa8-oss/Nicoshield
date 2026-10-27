# Nico Shield

Landing page e-commerce une page (`index.html` + `assets/`) qui vend la gamme Nicorette® au Maroc :
paiement à la livraison (COD), commande envoyée sur WhatsApp, public adulte 18+.
Pas de build : HTML/CSS/JS statique, GSAP via cdnjs. Tester avec `python3 -m http.server 8080`.

## Contexte métier
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
