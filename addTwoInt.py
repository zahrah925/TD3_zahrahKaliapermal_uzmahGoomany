#!/usr/bin/env python3

import sys

def add(a, b):
    a = int( sys.argv[1] )
    b = int( sys.argv[2] )
    return 0

if __name__=="__main__":
    if (len(sys.argv) > 3):
        print ("Erreur, entrez que 2 variables, svp!")
    elif (len(sys.argv) < 3):
        print("Erreur, entrez que 2 variables, svp!")
    else:
        print( sys.argv)
