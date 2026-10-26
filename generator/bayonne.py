#!/usr/bin/env python3
"""Affiche « prochain match » (1600x900).

Exemple : python generator/bayonne.py --out out/ubb-bayonne-annonce.png
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Fonts, canvas, center_text, signature, WHITE, GOLD


def render(out, fonts, competition, home, away, date, stade, W=1600, H=900):
    img, d = canvas(W, H)
    center_text(d, W, 60, f"PROCHAIN MATCH · {competition}", fonts("SemiBold", 52), GOLD)
    center_text(d, W, 150, home, fonts("Black", 260), WHITE)
    center_text(d, W, 415, f"vs  {away}", fonts("ExtraBold", 130), WHITE)
    d.rectangle([W / 2 - 260, 590, W / 2 + 260, 596], fill=GOLD)
    center_text(d, W, 620, date, fonts("Bold", 78), WHITE)
    center_text(d, W, 715, stade, fonts("SemiBold", 56), GOLD)
    signature(d, W, H, fonts("SemiBold", 34))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    img.save(out)
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", default="out/ubb-bayonne-annonce.png")
    p.add_argument("--fonts-dir", default=None, help="dossier des .ttf Barlow Condensed (défaut : ./fonts)")
    p.add_argument("--competition", default="TOP 14")
    p.add_argument("--home", default="UBB")
    p.add_argument("--away", default="BAYONNE")
    p.add_argument("--date", default="SAMEDI 31 OCTOBRE · 16H35")
    p.add_argument("--stade", default="STADE CHABAN-DELMAS")
    a = p.parse_args()
    print(render(a.out, Fonts(a.fonts_dir), a.competition, a.home, a.away, a.date, a.stade))


if __name__ == "__main__":
    main()
