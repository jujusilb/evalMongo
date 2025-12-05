from models import perso
from models import monstre
from models.perso import team
from models.monstre import list_monstre
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random
from models import perso
from models import monstre


score= 0
monstre=monstre.fetch_monster(list_monstre)

#annonce la victoire d'un joueur
def you_win():
    print("IN YOU_WIN")
    print("YOU WIN ! a bientot !²")

#annonce la defaite d'un joueur
def game_over():
    print("IN GAME_OVER")
    print("Vous avez perdu, a bientot !")
    return 0

def partie(team, list_monstre):
    print("IN PARTIE")
    while len(team)>0:
        tour(perso, monstre)
 
def attaque(attaquant, defenseur):
    print("IN ATTAQUE")
    coup =attaquant["ATK"]-defenseur["DEF"]
    defenseur["PV"] = defenseur["PV"]-coup
    print(f"{attaquant} envois une attaque a {defenseur} de {attaquant["ATK"]}pts")
    print(f"{defenseur} dispose de {defenseur["DEF"]} pts de defense")
    print(f"il lui reste donc {defenseur["PV"]}pts de vie")
        
def tour(perso, monstre):
    attaque(perso, monstre)
    monstre.check_monster(monstre)
    attaque(monstre, perso)
    perso.check_perso(perso)
    
def add_score(db, user, score):
    db.score.insert_one({"name":user, "score":score})
    
#verifie s'il le score est un high scode, si oui il l'envois en base
def stockage_score(db, high_score, user, score):
    print("IN STOCKAGE_SCORE")
    if not len(high_score)>0:
        add_score
        return ""
    for item in high_score:
        if score >  item["score"]:
            update_score(db, item, user, score)
        
def update_score(db, item, user, score):
    print("IN UPDATE_SCORE")
    db.score.update_one(
        {"_id": ObjectId(item["_id"])}, 
        {"$set": {"name":user, "score":score}}
    )
    
tour(monstre, perso)
#monstre.delete_monster(db, monstre)
