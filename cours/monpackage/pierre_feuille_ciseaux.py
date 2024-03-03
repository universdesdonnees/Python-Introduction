#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import random

# Jeu du pierre feuille ciseaux 

def obtenir_choix():
    # controle du choix utilisateur 
    choix_utilisateur = str(input("Saisir votre choix (pierre, feuille ou ciseaux): "))          
    while choix_utilisateur not in ["pierre", "feuille", "ciseaux"]:        
        choix_utilisateur = str(input("Choix invalide. Saisir choix (pierre, feuille ou ciseaux): ")) 
    # choix aléatoire ordinateur
    choix_ordinateur =  random.choice( ["pierre", "papier", "ciseaux"])
    return {'utilisateur' : choix_utilisateur,'ordinateur' : choix_ordinateur }   

def comparaison(ordi, user):
    if  ordi == user:
        resultat = "Egalité !"
    elif ordi == "pierre" and user == "feuille" or ordi == "feuille" and user == "ciseaux" or ordi == "ciseaux" and user == "pierre":
        resultat = "Victoire !"
    else:
        resultat = "Défaite !"
    return resultat

def jeu():
    print('*************************************************************' )
    print('***** Bienvenue dans le jeu du Pierre, Feuille, Ciseaux *****' )
    print('*************************************************************\n' )
    choix = obtenir_choix()
    print(f"l'ordinateur a choisi : {choix['ordinateur']} et l'utilisateur : {choix['utilisateur']}")
    print('\n*************************\n' )
    resultat_jeu = comparaison(ordi = choix["ordinateur"], user = choix["utilisateur"])
    return print(f"Resultat : {resultat_jeu}")

if __name__ == "__main__":
    jeu()