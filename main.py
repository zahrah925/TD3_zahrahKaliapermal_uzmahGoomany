<<<<<<< HEAD
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
=======
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
>>>>>>> bd4cbc831857045d00d413a66279b5f6fe7acda0
