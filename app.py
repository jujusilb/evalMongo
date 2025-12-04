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

DB = get_database()

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


#verifie s'il le score est un high scode, si oui il l'envois en base
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

#recupere les meilleurs score 
def get_high_score(db):
    print("GET_HIGH_SCORE")
    return db.score.find()


#fonction principale
def main():
    print("IN MAIN")
    db =get_database()
    choice=1
    if choice ==1:
        team =[]
        #username =get_username()
        perso.about_perso(db, team)
    elif choice ==2:
        print ("les highScire vont arriver vite !")
    elif choice == 3:
        print ("a tres vite !")
        return 0
    
main()

#compte le nombre de monstre en base
def count_monster(db):
    print("IN COUNT_MONSTER")
    return db.monstres.count_documents({})

#recupere la liste des monstre en database
def get_list_monster(db):
    print("IN GET_LIST_MONSTER")
    return list(db.monstre.find())
    
def about_monster(db):
    print("IN ABOUT_MONSTER")
    list_monstre =get_list_monster(DB)
    
    
#recupere un monstre aleatoirement depuis la base
def fetch_monster(db):
    print("IN FETCH_MONSTER")
    max_count =count_monster(db)
    alea =random.randint(1, max_count)
    return ({"_id": ObjectId(alea)})

#supprime un monstre de la base
def delete_monster(db, monstre):
    print("IN DELETE_MONSTER")
    db.delete_one({"_id", ObjectId(monstre)})


#retire un perso de l'equipe
def pop_perso(team, perso):
    print("IN POP_PERSO")
    team.pop(team.index(perso))

#verifie la santé d'un perso
def check_perso(team, item):
    print("IN DEFAIE_PËRSO")
    if perso["PV"] <=0:
        pop_perso(team, perso)
    check_team(team)

#verifie si l'equipe n'est pas vide
def check_team(team):
    print("IN CHECK_TEAM")
    if len(team) == 0:
        game_over()
       

def check_monster(db, monstre):
    print("IN DEFAITE_MONSTRE")


#annonce la victoire d'un joueur
def you_win():
    print("IN YOU_WIN")
    print("YOU WIN ! a bientot !²")

#annonce la defaite d'un joueur
def game_over():
    print("IN GAME_OVER")
    print("Vous avez perdu, a bientot !")
    return 0



def partie(team, db):
    print("IN PARTIE")
    while count_monster(db) >0:
        monstre = fetch_monster(db)

        delete_monster(db, monstre)


#attaque du monstre
def attaque_monstre(monstre, perso):
    print("IN ATTAQUE_MONSTRE")

def attaque(attaquant, defenseur):
    print("IN ATTAQUE")
    # dommage = attaque - defenseur
    coup =attaquant["ATK"]-defenseur["DEF"]
    if coup >=0:
        defenseur["PV"] = defenseur["PV"]-coup
    


    
    #tu veux pas d'abord le voir en entier? je opense avoir repondu au vbesoin...
    
    #
    ## ok 
    #
    #EN gros, j'ai une fonction (enfin 2)
    #delete perso et delete monster
    # monster est en bdd
    #perso est en team(lpca)
    #