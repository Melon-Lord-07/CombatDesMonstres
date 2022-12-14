"""
Sandra Nitchi, 405
TP3 - combat des monstres
Ceci est un jeu où le joueur roule 2 dés pour combattre des montres dans une labyrinthe
"""
import random

def debut():
    """
    definit les valeurs du debut du jeu (0 combats, niveau de vie de 20)
    """
    global niveau_vie, numero_adversaire, nombre_victoires, nombre_defaites, nombre_victoires_consecutives
    niveau_vie = 20
    numero_adversaire = 0
    nombre_victoires = 0
    nombre_defaites = 0
    nombre_victoires_consecutives = 0


def action():
    """
    code qui definit les quatre actions que le joueur peut faire: combattre, contourner, afficher les règles, ou quitter
    """
    print(f"Niveau de vie: {niveau_vie}"
          f"Vous tombez sur un adversaire de force {force_adversaire}")

    global quoi_faire, numero_adversaire, nombre_victoires, nombre_defaites, nombre_victoires_consecutives, niveau_vie

    quoi_faire = int(input("Que voulez-vous faire ? \n1- Combattre cet adversaire \n2- Contourner cet adversaire et "
                           "aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie"))

    if quoi_faire == 1:
        numero_adversaire += 1
        print(f"Adversaire : {numero_adversaire}"
              f"\n Force de l'adversaire : {force_adversaire}"
              f"\n Ton niveau de vie: {niveau_vie}"
              f"\n combat {numero_adversaire}: {nombre_victoires} victoires et {nombre_defaites} defaites \n... ")
        score_de_1 = random.randint(1, 6)
        score_de_2 = random.randint(1, 6)
        score_de_totale = score_de_1 + score_de_2
        print(f"\nLancer du dé 1: {score_de_1}"
              f"\nLancer du dé 2: {score_de_2}"
              f"\nTotale: {score_de_totale}")

        if score_de_totale > force_adversaire:
            combat_statut = "victoire!"
            nombre_victoires_consecutives += 1
            nombre_victoires += 1
            niveau_vie += force_adversaire

            print(f"Dernier combat = {combat_statut}"
                  f"\nNiveau de vie = {niveau_vie}"
                  f"\nNombre de victoires consecutives = {nombre_victoires_consecutives}")

            if nombre_victoires % 3 == 0 and nombre_victoires != 0:
                print("\nBoss adversaire!")
                intense()
            else:
                normale()

        else:
            combat_statut = "défaite!"
            niveau_vie -= force_adversaire
            nombre_victoires_consecutives = 0
            nombre_defaites += 1
            print(f"Dernier combat = {combat_statut}")

            if niveau_vie > 0:
                print(f"Niveau de vie = {niveau_vie}")
                normale()
            else:
                print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s)."
                      "\nNouveau jeu!")
                debut()
                normale()

    elif quoi_faire == 2:
        niveau_vie -= 1
        print("Vous contournez l'adversaire au cout de 1 pt de vie"
              f"\nNiveau de vie = {niveau_vie}")

        if nombre_victoires_consecutives >= 3:
            print("\nBoss adversaire!")
            intense()
        else:
            normale()

    elif quoi_faire == 3:
        print("\nPour réussir un combat, il faut que la valeur des 2 dés lancés soit supérieure à la force de "
              "l’adversaire."
              "\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
              "\nUne défaite a lieu lorsque la valeur des 2 dés lancés par l’usager est inférieure ou égale à la force "
              "de"
              " l’adversaire. "
              "\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
              "\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0."
              "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité "
              "de 1 point de vie.\n")
        action()

    else:
        print("Merci et au revoir...")


def normale():
    """
    génère la force de l'adversaire normale
    """
    global force_adversaire
    force_adversaire = random.randint(1, 5) + random.randint(1, 5)
    action()


def intense():
    """
    génère la force de l'adversaire boss, rencontré après 3 victoires consécutives
    """
    global force_adversaire
    force_adversaire = random.randint(10, 11)
    action()


debut()
normale()
