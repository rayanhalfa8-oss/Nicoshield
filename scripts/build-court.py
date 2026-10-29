#!/usr/bin/env python3
"""Version d'essai « courte » : court.html, générée depuis index.html.
Les offres remontent juste après le calculateur, les sections d'argumentation sont allégées
(graphique, barre et chronologie santé retirés, Ramadan seul conservé), détails produit repliés,
dernier appel supprimé. Posologie, précautions, porte d'âge et mentions légales sont conservées."""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
src = sys.argv[1] if len(sys.argv) > 1 else "index.html"
dst = sys.argv[2] if len(sys.argv) > 2 else "court.html"
html = (root / src).read_text()

def cut(s, start, end, keep_end=True):
    a = s.index(start); b = s.index(end, a)
    return s[:a] + (s[b:] if keep_end else s[b + len(end):])

head, rest = html.split("<main id=\"main\">", 1)
body, tail = rest.split("</main>", 1)
marks = re.findall(r"<!-- ([A-ZÉÈ ]+) -->", body)
parts = {}
for i, m in enumerate(marks):
    a = body.index(f"<!-- {m} -->")
    b = body.index(f"<!-- {marks[i + 1]} -->") if i + 1 < len(marks) else len(body)
    parts[m] = body[a:b].rstrip() + "\n\n"

parts["PROBLÈME"] = cut(parts["PROBLÈME"], '    <div class="craving rv">', '    <div class="triggers">')
parts["MÉTHODE"] = cut(parts["MÉTHODE"], '    <div class="chewbar rv"', "  </div>\n</section>")
ram = re.search(r'      <article class="angle angle--ram rv">.*?</article>\n', parts["CORPS"], re.S).group(0)
parts["CORPS"] = ('<!-- CORPS -->\n<section class="sec" id="corps" style="padding-top:0">\n  <div class="wrap">\n'
                  + ram.replace("      <article", '    <article style="max-width:640px;margin-inline:auto"', 1).replace("\n      ", "\n    ")
                  + "  </div>\n</section>\n\n")
prod = parts["PRODUIT HÉROS"]
t0 = prod.index('      <table class="spec rv">'); t1 = prod.index("      </table>", t0) + len("      </table>")
prod = prod[:t0] + '      <details class="specd"><summary>Voir les détails du produit</summary>\n' + prod[t0:t1] + "\n      </details>" + prod[t1:]
parts["PRODUIT HÉROS"] = prod
# les 4 garanties répètent le bandeau d'avantages placé au-dessus des packs
parts["OFFRES"] = cut(parts["OFFRES"], '    <div class="guar">', "  </div>\n</section>")

parts["MÉTHODE"] = parts["MÉTHODE"].replace('    <div class="method__grid">', '    <span class="swipe" aria-hidden="true">Faites glisser →</span>\n    <div class="method__grid">', 1)
order = ["HÉROS", "CALCULATEUR", "OFFRES", "COMMANDE", "PRODUIT HÉROS", "PROBLÈME", "MÉTHODE", "CORPS", "FAQ"]
assert set(order) | {"CTA FINAL"} == set(parts), parts.keys()
css = ('<style id="court">.specd{margin-bottom:1rem}.specd>summary{cursor:pointer;font-weight:600;padding:.8rem 0;min-height:44px}'
       '#probleme .triggers{margin-top:1rem}'
       # téléphone : carrousels horizontaux pour la méthode et les moments, cartes de packs allégées
       '@media (max-width:639px){'
       '.method__grid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:.7rem;margin-inline:calc(var(--g)*-1);padding:0 var(--g) .4rem;scrollbar-width:none}'
       '.method__grid::-webkit-scrollbar{display:none}'
       '.mstep{flex:0 0 78%;scroll-snap-align:start;padding:1.1rem;gap:.55rem}.mstep svg.ill{width:44px;height:44px}.mstep h3{font-size:1.2rem}.mstep p{font-size:.9rem}'
       '.tchips{flex-wrap:nowrap;overflow-x:auto;margin-inline:calc(var(--g)*-1);padding:0 var(--g) .3rem;scrollbar-width:none}.tchips::-webkit-scrollbar{display:none}.tchip{flex:none}'
       '.plan[data-plan]:not(.plan--best) ul,.plans--plq .plan ul{display:none}'
       '.plan[data-plan]:not(.plan--best){padding:1.3rem 1.1rem 1.1rem;gap:.6rem}'
       '.plan[data-plan]:not(.plan--best) .plan__price b{font-size:2.2rem}'
       '.hero .facts dd{font-size:.78rem}.hero .facts div{padding-top:.7rem}'
       '.sec{padding-block:clamp(2.6rem,9vw,4rem)}'
       '.swipe{display:block;font-size:.8rem;color:var(--muted);margin:-.3rem 0 .6rem}}'
       '.swipe{display:none}'
       '@media (max-width:559px){.promo{grid-template-columns:1fr 1fr;gap:.4rem}.promo__it{grid-template-columns:1fr;padding:.6rem .7rem;row-gap:.2rem}.promo__ic{grid-row:auto;font-size:1.2rem}.promo__it b{font-size:.85rem}.promo__it small{font-size:.72rem}}</style>\n</head>')
out = head.replace("</head>", css, 1) + '<main id="main">\n' + "".join(parts[k] for k in order) + "</main>" + tail
(root / dst).write_text(out)
print(root / dst)
