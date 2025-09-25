from tools import checkIntPos


def chain_mess():
    print("TP1_4")
    message = input("Entrez le message à souhaiter : ")

    nombre = checkIntPos()

    amis = []
    for i in range (1, nombre + 1):
        nom = input(f"Nom de l'ami {i}").strip()
        if nom:
            amis.append(nom)

    print("Messages personalisés :")
    for ami in amis:
        print(f"Cher {ami}, {message}")