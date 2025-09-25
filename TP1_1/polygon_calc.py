import json
import re, math
from pathlib import Path

from tools import checkIntBetweenXandY, checkIntPos, checkFLoatPos


def polygon_calc():
    print("TP1_1 et TP1.2")
    chemin_json = Path(__file__).parent / 'shapes.json'

    with open(chemin_json, 'r', encoding="utf-8") as f:
        data = json.load(f)

    shapes = data["shapes"]

    print("De quelle forme voulez-vous compléter la formule :")
    for i, shape in enumerate(shapes, start=1):
        print(f"{i}. {shape['nom']}")

    choix = checkIntBetweenXandY(1, len(shapes))

    shape = shapes[choix - 1]

    print(f"Vous avez choisi {shape['nom']}.")
    treat_formula(shape["formula"])

def treat_formula(formula: str):
    # Extraction des variables (lettres seules ET SANS DOUBLONS)
    variables = sorted(set(re.findall(r"\b[a-zA-Z]\b", formula)))

    # Remplissage des valeurs par l'utilisateur
    values = {"π": math.pi}
    for var in variables:
        if var not in values:
            print(f"Entrez une valeur pour {var}.")
            values[var] = checkFLoatPos()


    # Mise à éxécution de la formule
    try:
        result = eval(formula, {}, values)
    except Exception as e:
        print("Erreur lors de l'évaluation :", e)
        return None

    # Display de fin
    print(f"\nFormule : {formula}")
    print(f"Valeurs : {values}")
    print(f"Résultat = {result}")
    return result