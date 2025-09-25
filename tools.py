
# On vérifie que la valeur que l'on veut exploiter rentre dans nos attentes
def checkIntBetweenXandY(X, Y):
    while 1:
        userInput = input("Entrez une valeur entre " + str(X) + " et " + str(Y) + "\n")
        try:
            value=int(userInput)
            if X <= value <= Y:
                return value
            else:
                print("Votre choix doit rentrer dans les valeurs autorisées")
        except ValueError:
            print("Votre choix doit être un entier")

def checkIntPos():
    while 1:
        userInput = input("Entrez un entier positif")
        try:
            value=int(userInput)
            if value > 0:
                return value
            else:
                print("Votre choix doit être une valeur positive")
        except ValueError:
            print("Votre choix doit être un entier")

def checkFLoatPos():
    while 1:
        userInput = input("Entrez un nombre flottant positif")
        try:
            value=float(userInput)
            if value > 0:
                return value
            else:
                print("Votre choix doit être une valeur positive")
        except ValueError:
            print("Votre choix doit être un flottant")

def checkOuiOuNon(question) -> bool:
    while 1:
        reponse = input(question + "Oui ou non ?").strip().lower()
        if reponse in ["o", "oui", "y", "yes"]:
            return True
        elif reponse in ["n", "non", "no"]:
            return False
        else:
            print("Veuillez rentrer une réponse valide.")
