#!/usr/bin/env python3
"""Construit deploy/artifact.html : index.html avec les images de assets/ intégrées
en data URI, pour l'aperçu artifact (qui ne charge pas les fichiers assets/ séparés)."""
import base64, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()

def inline(m):
    f = root / m.group(0)
    return "data:image/webp;base64," + base64.b64encode(f.read_bytes()).decode()

# (?<!/) : on garde les URL absolues (og:image, JSON-LD) telles quelles
out = re.sub(r"(?<!/)assets/[\w.-]+\.webp", inline, html)
dest = root / "deploy" / "artifact.html"
dest.parent.mkdir(exist_ok=True)
dest.write_text(out)
print(dest, f"{len(out) // 1024} Ko", "restants :", re.findall(r"(?<!/)assets/[\w.-]+", out))
