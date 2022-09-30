"""
Sandra Nitchi, 405
TP3 - combat des monstres
"""
import random

niveau_vie = 20

def action():

    force_adversaire = random.randint(1,5)

    print(f"vous tombez sur un adversaire de force {force_adversaire}")

    quoi_faire = int(input("Que voulez-vous faire ? \n1- Combattre cet adversaire \n2- Contourner cet adversaire et "
                           "aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie"

    if quoi_faire == 1:
        print("option 1")
    elif quoi_faire == 2:
        print("option 2")
    elif quoi_faire == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
              "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de"
              " l’adversaire. "
              "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
              "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité "
              "de 1 point de vie.")


    else:
        print("option 4")

action()

