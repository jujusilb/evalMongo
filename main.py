import sys
from bson.objectid import ObjectId
from datetime import datetime
import random
from models import perso
from models import monstre
import file_games
import db




MAIN_MENU= [
        "1. Démarrer le jeu",
        "2. Afficher le classement",
        "3. Quitter"
    ]

MAIN_MENU_LEN = len(MAIN_MENU)

#agrege toute la partie du menu principale
def main_menu():
    print("IN MAIN_MENU")
    show_main_menu()
    return get_choice_main_menu(MAIN_MENU_LEN)

#affiche le menu principale
def show_main_menu():
    print("IN SHOW_MENU")
    for item in MAIN_MENU:
        print(item)

#recupere le choix du joueur au menu principale
def get_choice_main_menu(max):
    print("IN GET_CHOICE_MAIN_MENU")
    choice =0
    while choice < 1 or choice > max :
        choice=int(input("quel est votre choix?"))
    return choice

DB = db.get_database()

#recupere le pseudo du joueur
def get_username():
    print("IN GET_USERNAME")
    username =input ("quel sera votre username?")
    return username


#recupere les meilleurs score 
def get_high_score(db):
    print("GET_HIGH_SCORE")
    return db.score.find()

#fonction principale
def main():
    print("IN MAIN")

    choice=1
    if choice ==1:
        
        team =[]
        list_monstre =[]
        #username =get_username()
        perso.about_perso(DB, team)
        monstre.about_monster(list_monstre)
        for item in team:
            print(item)
        for item2 in list_monstre:
            print("item2")
        file_games.partie(team, list_monstre)
    elif choice ==2:
        print ("les highScire vont arriver vite !")
    elif choice == 3:
        print ("a tres vite !")
        return 0
global score
main()