#!/usr/bin/env python3
"""Infographie « L'infirmerie » classée par poste (1200x1500), à partir d'un fichier JSON.

Exemple : python generator/infirmerie.py data/infirmerie-2026-10-26.json --out out/infirmerie.png
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Fonts, canvas, center_text, signature, WHITE, GOLD, SOFT, CARD

W, H = 1200, 1500
X0 = 70
CARD_H, CARD_GAP, HEADER_H = 122, 24, 62


def render(data, out, fonts):
    img, d = canvas(W, H)
    center_text(d, W, 50, data.get("kicker", "POINT MÉDICAL · TOP 14"), fonts("SemiBold", 44), GOLD)
    center_text(d, W, 105, data.get("title", "L'INFIRMERIE"), fonts("Black", 170), WHITE)
    center_text(d, W, 300, data["subtitle"], fonts("SemiBold", 42), WHITE)
    d.rectangle([W / 2 - 220, 368, W / 2 + 220, 374], fill=GOLD)
    if data.get("context"):
        center_text(d, W, 388, data["context"], fonts("SemiBold", 36), SOFT)

    boxw = W - 2 * X0
    y = 462
    for group in data["groups"]:
        d.rectangle([X0, y, X0 + 10, y + 52], fill=GOLD)
        d.text((X0 + 28, y - 2), group["position"].upper(), font=fonts("ExtraBold", 46), fill=GOLD)
        y += HEADER_H
        for pl in group["players"]:
            d.rounded_rectangle([X0, y, X0 + boxw, y + CARD_H], radius=14, fill=CARD, outline=GOLD, width=2)
            d.text((X0 + 30, y + 8), pl["name"], font=fonts("Black", 56), fill=WHITE)
            ret = "Retour : " + pl.get("return", "non communiqué")
            rf = fonts("ExtraBold", 32)
            d.text((X0 + boxw - 30 - d.textlength(ret, font=rf), y + 24), ret, font=rf, fill=GOLD)
            d.text((X0 + 30, y + 72), pl["injury"], font=fonts("SemiBold", 36), fill=SOFT)
            y += CARD_H + CARD_GAP
    footer_top = H - 118
    if y > footer_top:
        raise SystemExit(f"Trop de joueurs : le contenu descend à y={y}, limite {footer_top}.")
    for i, line in enumerate(data.get("footer", [])[:2]):
        d.text((X0, footer_top + 36 * i), line, font=fonts("SemiBold", 28), fill=SOFT)
    signature(d, W, H, fonts("SemiBold", 34))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    img.save(out)
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("data", help="fichier JSON décrivant l'infirmerie (voir data/)")
    p.add_argument("--out", default="out/infirmerie.png")
    p.add_argument("--fonts-dir", default=None, help="dossier des .ttf Barlow Condensed (défaut : ./fonts)")
    a = p.parse_args()
    with open(a.data, encoding="utf-8") as f:
        data = json.load(f)
    print(render(data, a.out, Fonts(a.fonts_dir)))


if __name__ == "__main__":
    main()
