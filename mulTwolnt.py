#!/usr/bin/env python3

import sys

def mul():
    x = int( sys.argv[1] )
    y = int( sys.argv[2] )
    print(x, y)
    return 0

if __name__=="__main__":
    if (len(sys.argv) == 1):
        print("Veuillez inserer 2 valeurs.")
        x = int(input("Premiere valeur: "))
        y = int(input("Deuxieme valeur: "))
        print(x, y)

    elif (len(sys.argv) == 2):
        print("Veuillez inserer la 2eme valeur.")
        x = int( sys.argv[1] )
        y = int(input("La deuxieme valeur: "))
        print(x, y)

    elif (len(sys.argv) > 3):
        print("Erreur! Veuillez recommencer et inserer que 2 valeurs.")

    else:
        mul()
