import random
import string
from enum import nonmember

from tools import checkIntBetweenXandY, checkOuiOuNon


def passwd_gen():
    print("TP1_5")

    MIN = 8
    MAX = 25

    passwd_len = checkIntBetweenXandY(MIN, MAX)

    include_lower = checkOuiOuNon("Inclure des lettres minuscules ? ")
    include_upper = checkOuiOuNon("Inclure des lettres majuscules ? ")
    include_digits = checkOuiOuNon("Inclure des chiffres ? ")
    include_special = checkOuiOuNon("Inclure des symboles spéciaux ? ")

    lowercase = string.ascii_lowercase if include_lower else ""
    uppercase = string.ascii_uppercase if include_upper else ""
    digits = string.digits if include_digits else ""
    special = "@#$%^&*()" if include_special else ""

    all_included = lowercase + uppercase + digits + special

    if not all_included:
        print("Vous devez choisir au moins une catégorie de caractères.")
        return None

    passwd_composition = []

    for _ in range(passwd_len):
        passwd_composition.append(random.choice(all_included))

    password = ''.join(passwd_composition)
    print("Voici votre mot de passe : ", password)
