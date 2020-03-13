#!/user/bin/evn python3
#import addTwoInt addTwoInt.add(a, b)
from addTwoInt import add

import sys

if __name__=="__main__":

    if (len(sys.argv) > 3):
        print ("Erreur, entrez que 2 variables, svp!")

    elif (len(sys.argv) == 1):
        print("Erreur, entrez deux variables, svp!")
        a = int(input("Premier valeur : "))
        b = int(input("Deuxieme valeur : "))
        print( add(a, b) )

    elif (len(sys.argv) == 2):
        print("Erreur, entrez encore une valeur, svp!")
        b = input("Deuxieme valeur : ")
        a = int( sys.argv[1] )
        b = int(b)
        print( add(a, b))

    else:
        a = int( sys.argv[1] )
        b = int( sys.argv[2] )
        print( add(a, b) )

if(len(sys.argv) < 4):
    print("Voulez vous additioner les 2 valeurs? (o-oui / n-non)")
    reponse = input()
    if(reponse == "o"):
        print(a," + ", b," = ", a+b)
    else:
        print("OK!")
