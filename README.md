# Visuels — générateur d'infographies rugby

Petit projet Python qui génère les visuels du compte fan **@UBBAllezAllez**
(supporters de l'Union Bordeaux Bègles) : affiches de match, infirmerie par poste, etc.

Style maison : fond bordeaux en dégradé avec rayures diagonales, bande et accents dorés,
texte blanc en Barlow Condensed, signature en bas à droite. Aucun logo officiel n'est utilisé.

## Contenu du dépôt

| Chemin | Rôle |
| --- | --- |
| `generator/common.py` | Module commun : fond, rayures, bande dorée, polices, texte centré, signature |
| `generator/bayonne.py` | Affiche « prochain match » (1600x900), textes paramétrables |
| `generator/infirmerie.py` | Infographie « L'infirmerie » classée par poste (1200x1500), alimentée par un JSON |
| `data/` | Exemples de données (ex. `infirmerie-2026-10-26.json`) |
| `images/` | Visuels déjà publiés (leurs URL restent stables, ne pas les déplacer) |

## Installation

Python 3.9 ou plus récent.

```bash
pip install pillow
# ou
pip install -r requirements.txt
```

### Polices

Les visuels utilisent **Barlow Condensed** (graisses Black, ExtraBold, Bold et SemiBold),
publiée sous licence **SIL Open Font License (OFL)**. Les fichiers de police ne sont pas
versionnés : télécharge la famille depuis Google Fonts
(<https://fonts.google.com/specimen/Barlow+Condensed>) et copie les fichiers `.ttf`
(par ex. `BarlowCondensed-Black.ttf`) dans un dossier `fonts/` à la racine du dépôt.

Tu peux aussi indiquer un autre dossier avec l'option `--fonts-dir` ou la variable
d'environnement `UBB_FONTS_DIR`.

## Usage

```bash
# Affiche de match (valeurs par défaut : UBB vs Bayonne)
python generator/bayonne.py --out out/ubb-bayonne-annonce.png

# Autre affiche
python generator/bayonne.py --away "TOULOUSE" --date "SAMEDI 7 NOVEMBRE · 21H05" \
    --stade "STADE CHABAN-DELMAS" --out out/ubb-toulouse.png

# Infirmerie à partir d'un fichier de données
python generator/infirmerie.py data/infirmerie-2026-10-26.json --out out/infirmerie.png
```

Les images sont écrites dans `out/` (ignoré par git).

### Format du JSON d'infirmerie

```json
{
  "subtitle": "avant UBB - Bayonne · samedi 31/10 · Chaban-Delmas",
  "context": "Forfaits et blessés du match à La Rochelle (19-25, 25/10)",
  "groups": [
    {"position": "3e ligne", "players": [
      {"name": "Prénom NOM", "injury": "Nature de la blessure", "return": "non communiqué"}
    ]}
  ],
  "footer": ["Ligne 1", "Ligne 2"]
}
```

Le script s'arrête avec un message clair si la liste est trop longue pour tenir sur l'image.

## Licence

Code sous licence MIT (voir `LICENSE`). Les polices Barlow Condensed restent sous leur
propre licence OFL.
