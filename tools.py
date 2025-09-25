
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
