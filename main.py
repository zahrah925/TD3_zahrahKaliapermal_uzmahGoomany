#!/usr/bin/evn python3

import sys

# from mulTwolnt import mul --> use to import function mul() from mulTwolnt.py

if __name__ == "__main__":
    try:
        if (len(sys.argv) == 1):
            print("Veuillez inserer 2 valeurs.")
            x = int(input("Premiere valeur: "))
            y = int(input("Deuxieme valeur: "))
            print(x, y)

        elif (len(sys.argv) == 2):
            print("Veuillez inserer la deuxieme valeur.")
            x = int(sys.argv[1])
            y = int(input("La deuxieme valeur: "))
            print(x, y)

        elif (len(sys.argv) > 3):
            print("Erreur! Veuillez recommencer et inserer que 2 valeurs.")

        else:
            # mul()  -->  cannot use since in imported function there is return 0, x and y cannot be used
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            print(x, y)

    finally:
        if (len(sys.argv) < 4):
            print("Voulez-vous multiplier les deux valeurs? (O(Oui)/N(Non))")
            decision = input()

            if (decision == "O") | (decision == "o"):
                raiponse = x * y
                print("La multiplication de", x, "et", y, "est", raiponse, ".")
                print("Fin")

            elif (decision == "N") | (decision == "n"):
                print("Fin")

            else:
                print("Erreur!")

        else:
            print("Fin")
