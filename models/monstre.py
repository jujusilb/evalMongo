import random
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import file_games 
#from game import score
import db

#compte le nombre de monstre en base
def count_monster(list_monstre):
    print("IN COUNT_MONSTER")
    return len(list_monstre)-1

def about_monster(list_monstre):
    print("IN ABOUT_MONSTRE")
    list_monstre.extend(get_list_monster(db.get_database()))



#recupere la liste des monstre en database
def get_list_monster(db):
    print("IN GET_LIST_MONSTER")
    return list(db.monstres.find())
     


#recupere un monstre aleatoirement depuis list_monstre
def fetch_monster(list_monstre):
    print("IN FETCH_MONSTER")
    unSeulMonstre =random.choice(list_monstre)
    list_monstre.remove(unSeulMonstre)
    return unSeulMonstre

#supprime un monstre de la base
def delete_monster(db, monstre):
    print("IN DELETE_MONSTER")
    db.delete_one({"_id", ObjectId(monstre)})

#verifie la santé d'un perso
def check_monster(list_monstre, monstrePNJ):
    print("IN CHECK_MONSTER")
    
    if monstrePNJ["PV"] <=0:
       return True
    return False
        

def check_list_monstre(list_monstre):
    print("IN CHECK_LIST_MONSTER")
    if len(list_monstre) <1:
        file_games.you_win()
    
#retire un perso de l'equipe
def pop_monster(list_monstre, monstrePnj):
    print("IN POP_monstre")
    print(f"degage {monstrePnj["name"]}")
    for i, item in enumerate(list_monstre):
        if item["name"] == monstrePnj["name"]:
            list_monstre.pop(i)
            break 
    print ("len list_monstre")
    print(len(list_monstre))
    print(list_monstre)
    #list_monstre.remove(list_monstre.index(monstrePnj))

