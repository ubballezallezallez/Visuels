"""Briques communes des visuels : fond bordeaux en dégradé, rayures diagonales,
bande dorée, polices Barlow Condensed et signature."""
import os
from PIL import Image, ImageDraw, ImageFont

BORD = (94, 18, 44)
BORD2 = (60, 8, 28)
WHITE = (255, 255, 255)
GOLD = (214, 175, 90)
SOFT = (235, 215, 220)
CARD = (40, 4, 18)

SIGNATURE = "@UBBAllezAllez"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FONTS_DIR = os.path.join(REPO_ROOT, "fonts")


class Fonts:
    """Charge les graisses de Barlow Condensed depuis un dossier (par défaut ./fonts)."""

    def __init__(self, fonts_dir=None):
        self.dir = fonts_dir or os.environ.get("UBB_FONTS_DIR") or DEFAULT_FONTS_DIR
        self._cache = {}

    def __call__(self, weight, size):
        key = (weight, size)
        if key not in self._cache:
            path = os.path.join(self.dir, f"BarlowCondensed-{weight}.ttf")
            if not os.path.exists(path):
                path = os.path.join(self.dir, "BarlowCondensed-Bold.ttf")
            if not os.path.exists(path):
                raise SystemExit(
                    f"Police introuvable dans {self.dir!r}. Télécharge Barlow Condensed "
                    "(Google Fonts) et place les .ttf dans fonts/, ou utilise --fonts-dir.")
            self._cache[key] = ImageFont.truetype(path, size)
        return self._cache[key]


def canvas(width, height, stripe_step=90, band=22):
    """Crée l'image de base : dégradé, rayures diagonales et bande dorée à gauche."""
    img = Image.new("RGB", (width, height), BORD)
    d = ImageDraw.Draw(img)
    for y in range(height):
        t = y / height
        d.line([(0, y), (width, y)], fill=tuple(int(BORD[i] * (1 - t) + BORD2[i] * t) for i in range(3)))
    stripe = tuple(min(255, v + 8) for v in BORD2)
    for x in range(-height, width, stripe_step):
        d.polygon([(x, height), (x + 30, height), (x + 30 + height * 0.6, 0), (x + height * 0.6, 0)], fill=stripe)
    d.rectangle([0, 0, band, height], fill=GOLD)
    return img, d


def center_text(d, width, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((width - w) / 2, y), text, font=font, fill=fill)


def signature(d, width, height, font, text=SIGNATURE):
    d.text((width - d.textlength(text, font=font) - 40, height - 60), text, font=font, fill=WHITE)
