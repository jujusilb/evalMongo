import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random

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

def main_menu():
    print("IN MAIN_MENU")
    show_main_menu()
    return get_choice_main_menu(MAIN_MENU_LEN)

def show_main_menu():
    print("IN SHOW_MENU")
    for item in MAIN_MENU:
        print(item)


def get_choice_main_menu(max):
    print("IN GET_CHOICE_MAIN_MENU")
    choice =0
    while choice < 1 or choice > max :
        choice=int(input("quel est votre choix?"))
    return choice


def get_username():
    print("IN GET_USERNAME")
    username =input ("quel sera votre username?")
    return username

def about_perso(db, team):
    print("IN PERSO")
    perso=1
    list_perso =get_list_perso(db)
    #team =show_perso(list_perso, team, perso)
    team =create_team(list_perso, team, perso)

def show_team(team):
    print("IN SHOW_TEAM")
    print("VOICI L'EQUIPE")
    for item in team:
        print(item)

def show_perso(list_perso, team, nb):
    print("IN SHOW_PERSO")
    for item in list_perso:
        print(f"Nom :{item["name"]}, Defense :{item["DEF"]}, Attaque :{item["ATK"]}, Points de vie :{item["PV"]}")
    temp =get_choice_perso(nb)
    #team =create_team(list_perso, team, nb)
    return temp

def get_list_perso(db):
    print("IN GET_LIST_PERSO")
    return list(db.persos.find())
    
def get_alea_monstre(db):
    print("IN GET_LIST_MONSTRE")
    alea =random.radint(1, 10)
    return list(db.monstres.find())

def check_array(list_perso, string):
    print("IN CHECK_ARRAY")
    find=False
    for item in list_perso:
        if string == item["name"]:
            return True
    return False
     
def get_dico_in_array(list_perso, chosen): # ???
    print("IN GET_DICO_IN_ARRAY - ln 79")
    #print("boucle 0")
    #print (f"-- {list_perso} --")
    for item in list_perso:
        #print("boocle 1 ")
        #print(f"choser : {chosen}, item : {item}, itemName : {item["name"]}")
        if chosen ==item["name"]:
            #print(f"\nitem retourné = {item}")
            return item
        
team =[]
perso=1
perso_choisi =""      
def create_team(list_perso, team, perso):
    print("IN CREATE_TEAM")
    while len(team) < 3:
        tmp =show_perso(list_perso, team, perso)
        perso_choisi =check_exists(list_perso, tmp, perso)
        add_selection_in_team(list_perso, team, perso_choisi)
        perso =perso+1
    show_team(team)
    return team

def get_choice_perso(nbperso):
    print("IN GET_CHOICE_PERSO")
    string =input(f"choisissez un personnage {nbperso} :")
    return string
        
def check_exists(list_perso, string, perso):
    print("IN CHECK_EXISTS")
    bool =check_array(list_perso, string)  # ??
    while not bool:
        create_team(list_perso, team, perso)
    return string

def add_selection_in_team(list_perso, team, chosen):
    print("IN ADD_SELECTION_IN_TEAM")
    personnage =get_dico_in_array(list_perso, chosen)
    team.append(personnage)
    list_perso.pop(list_perso.index(personnage))

def stockage_score(db, high_score, user, score):
    print("IN STOCKAGE_SCORE")
    if not len(high_score)>0:
        db.score.insert_one({"name":user, "score":score})
        return ""
    for item in high_score:
        if score > item["score"]:
            db.score.update_one(
                {"_id": ObjectId(item["_id"])}, 
                {"$set": {"name":user, "score":score}}
            )
            return ""
        
def get_high_score(db):
    print("GET_HIGH_SCORE")
    return db.score.find()

def defaite_perso(team, item):
    print("IN DEFAIE_PËRSO")
    if item["PV"] <=0:
        team.pop(team.index(item))
    if len(team) == 0:
        game_over():

def defaite_monstre(db, item):
    print("IN DEFAITE_MONSTRE")
    if item["PV"] <=0:
        db.monstre.delete(db.monstres.index(item))
    if len(team) == 0:
        you_win()

def you_win():
    print("IN YOU_WIN")
    print("YOU WIN ! a bientot !²")

def game_over():
    print("IN GAME_OVER")
    print("Vous avez perdu, a bientot !")
    return 0

def main():
    print("IN MAIN")
    db =get_database()
    choice=1
    if choice ==1:
        #username =get_username()
        about_perso(db, team)
    elif choice ==2:
        print ("les highScire vont arriver vite !")
    elif choice == 3:
        print ("a tres vite !")
        return 0
    
main()