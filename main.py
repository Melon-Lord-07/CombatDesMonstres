"""
Sandra Nitchi, 405
TP3 - combat des monstres
"""
import random
import time


niveau_vie = 20
numero_adversaire = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0



def action():
    print(f"vous tombez sur un adversaire de force {force_adversaire}")

    global quoi_faire, numero_adversaire, nombre_victoires, nombre_defaites, nombre_victoires_consecutives, niveau_vie


    quoi_faire = int(input("Que voulez-vous faire ? \n1- Combattre cet adversaire \n2- Contourner cet adversaire et "
                           "aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie"))

    if quoi_faire == 1:  # combat
        numero_adversaire = numero_adversaire + 1
        print("option 1"
              f"\n Adversaire : {numero_adversaire}"
              f"\n Force de l'adversaire : {force_adversaire}"
              f"\n Ton niveau de vie: {niveau_vie}"
              f"\n combat {numero_adversaire}: {nombre_victoires} victoires et {nombre_defaites} defaites \n... ")
        time.sleep(5)
        score_de = random.randint(1,6)
        print(f"Lancer du dé: {score_de}")
        if score_de > force_adversaire:
            combat_statut = "victoire!"
            nombre_victoires_consecutives = nombre_victoires_consecutives + 1
            nombre_victoires = nombre_victoires + 1

            print(f"Dernier combat = {combat_statut}"
                  f"\nNiveau de vie = {niveau_vie}"
                  f"\nNombre de victoires consecutives = {nombre_victoires_consecutives}")
            action()


        else:
            combat_statut = "défaite!"
            niveau_vie = niveau_vie - force_adversaire
            nombre_victoires_consecutives = 0
            nombre_defaites = nombre_defaites + 1
            print(f"Dernier combat = {combat_statut}")
            if niveau_vie > 0:
                print(f"Niveau de vie = {niveau_vie}")
                action()
            else:
                print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")


    elif quoi_faire == 2:  # contourne adversaire
        niveau_vie = niveau_vie - 1
        print("Vous contournez l'adversaire au cout de 1 pt de vie"
              f"\nNiveau de vie = {niveau_vie}")
        action()

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
        print("Merci et au revoir...")


def jeu():
    global force_adversaire
    force_adversaire = random.randint(1,5)

    action()

jeu()


