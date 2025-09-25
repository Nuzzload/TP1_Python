from tools import checkIntPos


def sum_factor():
    print("TP1_3")
    value = checkIntPos()

    nombres = list(range(1, value + 1))

    somme = sum(nombres)

    factoriel = 1
    for x in nombres:
        factoriel *= x

    somme_str = " + ".join(map(str, nombres))
    fact_str = " * ".join(map(str, nombres))

    print(f"{somme_str} = {somme}")
    print(f"{somme} = {somme_str}")
    print(f"{fact_str} = {factoriel}")
    print(f"{factoriel} = {fact_str}")