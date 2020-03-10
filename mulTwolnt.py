#!/usr/bin/env python3

import sys

def mul(x, y):
    x = int( sys.argv[1] )
    y = int( sys.argv[2] )
    return 0

if __name__=="__main__":
    if (len(sys.argv) < 3):
        print("Erreur! Veuillez inserer 2 valeurs.")
    elif (len(sys.argv) > 3):
        print("Erreur! Veuillez inserer que 2 valeurs.")
    else:
        print(sys.argv)
