import argparse
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os

# Fonction pour lire le fichier XML au format donné
def lire_xml(fichier):
    arbre = ET.parse(fichier)
    racine = arbre.getroot()
    x = [float(elem.text) for elem in racine.find("xdata").findall("x")]
    y = [float(elem.text) for elem in racine.find("ydata").findall("y")]
    return x, y

# Définition des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Affiche un graphique depuis un fichier XML.")

parser.add_argument("fichier", help="Chemin vers le fichier XML")

# Paramètres optionnels
parser.add_argument("--title", help="Titre du graphique", default="Graphique de la fonction")
parser.add_argument("--xlabel", help="Nom de l'axe X", default="x")
parser.add_argument("--ylabel", help="Nom de l'axe Y", default="f(x)")
parser.add_argument("--xmin", type=float, help="Valeur minimale de l'axe X")
parser.add_argument("--xmax", type=float, help="Valeur maximale de l'axe X")
parser.add_argument("--ymin", type=float, help="Valeur minimale de l'axe Y")
parser.add_argument("--ymax", type=float, help="Valeur maximale de l'axe Y")
parser.add_argument("--style", choices=["solid", "dashed", "dotted"], default="solid", help="Style de ligne")
parser.add_argument("--output", help="Fichier image pour sauvegarder le graphique (ex: result.png)")

args = parser.parse_args()

# Lecture des données
x, y = lire_xml(args.fichier)

# Création du graphique
plt.figure(figsize=(10, 5))
plt.plot(x, y, label="f(x)", linestyle=args.style)

plt.title(args.title)
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
plt.grid(True)
plt.legend()

# Limites des axes si définies
if args.xmin is not None and args.xmax is not None:
    plt.xlim(args.xmin, args.xmax)
if args.ymin is not None and args.ymax is not None:
    plt.ylim(args.ymin, args.ymax)

plt.tight_layout()

# Sauvegarde ou affichage
if args.output:
    plt.savefig(args.output)
    print(f"Graphique sauvegardé dans : {args.output}")
else:
    plt.show()