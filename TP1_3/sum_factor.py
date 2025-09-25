from tools import checkIntPos


def sum_factor():
    print("TP1_3")
    value = checkIntPos()

    nombres = list(range(1, value + 1))

    somme = sum(nombres)

    factoriel = 1
    for x in nombres:
        factoriel *= x

    somme_string = " + ".join(map(str, nombres))
    factoriel_string = " * ".join(map(str, nombres))

    print(f"{somme_string} = {somme}")
    print(f"{somme} = {somme_string}")
    print(f"{factoriel_string} = {factoriel}")
    print(f"{factoriel} = {factoriel_string}")