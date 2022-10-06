"""
Sandra Nitchi, 405
TP3 - combat des monstres
"""
import random

niveau_vie = 20
numero_adversaire = 0


def action():
    print(f"vous tombez sur un adversaire de force {force_adversaire}")

    global quoi_faire

    quoi_faire = int(input("Que voulez-vous faire ? \n1- Combattre cet adversaire \n2- Contourner cet adversaire et "
                           "aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie"))

    if quoi_faire == 1:  # combat
        numero_adversaire = numero_adversaire + 1
        print("option 1"
              f"\n Adversaire : {numero_adversaire}"
              f"\n Force de l'adversaire : {force_adversaire}"
              f"\n Ton niveau de vie: {niveau_vie}")
#IM HERE!!!!!!!

        Adversaire: numero_adversaire
        Force
        de
        l’adversaire: force_adversaire
        Niveau
        de
        vie
        de
        l’usager: niveau_vie
        Combat
        numero_combat: nombre_victoires
        vs
        nombre_defaites

    elif quoi_faire == 2:  # contourne adversaire
        print("option 2")
    elif quoi_faire == 3:  # afficher les regles
        print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
              "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de"
              " l’adversaire. "
              "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
              "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité "
              "de 1 point de vie.\n")
        action()

    else:
        print("option 4")


def jeu():
    global force_adversaire
    force_adversaire = random.randint(1,5)

    action()

jeu()


