#!/usr/bin/env python3
"""Version d'essai « blanc et vert » : blanc.html, générée depuis index.html.
Fond blanc, thème clair forcé (pas de mode sombre), accents vert profond du bandeau défilant.
Relancer après chaque modification de index.html pour garder les deux versions identiques."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()

THEME = """<style id="theme-blanc">
:root,:root[data-theme="light"]{
  --paper:#FFFFFF; --surface:#FFFFFF; --sunk:#F1F7F3; --line:#DCE9E1; --ink:#0B1F1A; --muted:#4F635B;
  --green:#0F4A3F; --mint-soft:#E3F3EA; --btn:#0F4A3F; --btn-fg:#FFFFFF; --btn-hover:#072A23;
  --shadow:0 1px 2px rgb(7 42 35/.05),0 22px 44px -26px rgb(7 42 35/.28); color-scheme:light}
body{background:var(--paper)}
.plan,.pc,.calc__card,.order,.mstep,.angle,.promo__it,.pflip,.prod__main,details{border-color:var(--line)}
html:not([data-theme="dark"]) .offers{background:linear-gradient(#F1F7F3,#FFFFFF)}
html:not([data-theme="dark"]) .ftr{background:#F1F7F3}
</style>"""

assert html.count("<html") == 1 and html.count("</head>") == 1
html = html.replace('<html lang="fr-MA">', '<html lang="fr-MA" data-theme="light">')
html = html.replace('content="#F5EFE3" media="(prefers-color-scheme: light)"', 'content="#FFFFFF"')
html = html.replace('<meta name="theme-color" content="#08130F" media="(prefers-color-scheme: dark)">\n', '')
html = html.replace("</head>", THEME + "\n</head>")
(root / "blanc.html").write_text(html)
print(root / "blanc.html")
