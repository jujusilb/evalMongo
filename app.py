import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

def get_database():
    # URI local : "mongodb://localhost:27017"
    # Ou URI Atlas : "mongodb+srv://<user>:<password>@cluster0.mongodb.net/"
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["evalMongo"]  # Base de données "todo_db"
    return db

MAIN_MENU= [
        "1. Démarrer le jeu",
        "2. Afficher le classement",
        "3. Quitter"
    ]

def show_main_menu():
    for item in MAIN_MENU:
        print(item)


def get_choice_main_menu(max):
    choice =0
    while choice < max or choice > max :
        choice=int(input("quel est votre choix?"))
    return choice

def get_username():
    username =input ("quel sera votre username?")
    return username


show_main_menu()
get_choice_main_menu(len(MAIN_MENU))

def perso_choisis(db):
    db.persos.find()

    