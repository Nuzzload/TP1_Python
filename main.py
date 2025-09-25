from TP1_3.sum_factor import sum_factor
from TP1_4.chain_mess import chain_mess
from TP1_5.passw_gen import passwd_gen
from tools import *
from TP1_1.polygon_calc import *

menu = {
    1: polygon_calc,
    2: sum_factor,
    3: chain_mess,
    4: passwd_gen,
    5: exit
}

def main():
    while True:
        print("""Quel sous TP souhaitez vous charger ?
        1 - TP1_1 et TP1.2
        2 - TP1_3
        3 - TP1_4
        4 - TP1_5
        5 - Quitter
        """)
        key = checkIntBetweenXandY(1,5)

        if key in menu:
            menu[key]()






if __name__ == '__main__':
    main()

