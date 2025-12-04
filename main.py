import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random
from models import perso
from models import monstre



#se connecte a la db
def get_database():
    print("IN GET_DATABASE")
    # URI local : "mongodb://localhost:27017"
    # Ou URI Atlas : "mongodb+srv://<user>:<password>@cluster0.mongodb.net/"
    #client = MongoClient("mongodb://127.0.0.1:27017")
    client = MongoClient("mongodb+srv://jujusilb:Gaspesie@cluster0.revmtu2.mongodb.net/?appName=Cluster0")
    db = client["evalMongo"]  # Base de données "todo_db"
    return db



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

#recupere le pseudo du joueur
def get_username():
    print("IN GET_USERNAME")
    username =input ("quel sera votre username?")
    return username


#recupere les meilleurs score 
def get_high_score(db):
    print("GET_HIGH_SCORE")
    return db.score.find()

DB   =get_database()

#fonction principale
def main():
    print("IN MAIN")

    choice=1
    if choice ==1:
        team =[]
        #username =get_username()
        perso.about_perso(DB, team)
        monstre.about_monster(DB)
    elif choice ==2:
        print ("les highScire vont arriver vite !")
    elif choice == 3:
        print ("a tres vite !")
        return 0
    
main()