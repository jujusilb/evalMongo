import random
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
#import game
#from game import score

#compte le nombre de monstre en base
def count_monster(list_monstre):
    print("IN COUNT_MONSTER")
    return len(list_monstre)

def about_monster(db, list_monstre):
    print("IN ABOUT_MONSTRE")
    list_monstre.append(get_list_monster(db))



#recupere la liste des monstre en database
def get_list_monster(db):
    print("IN GET_LIST_MONSTER")
    return list(db.monstres.find())
     


#recupere un monstre aleatoirement depuis list_monstre
def fetch_monster(list_monstre):
    print("IN FETCH_MONSTER")
    max_count =count_monster(list_monstre)
    alea =random.randint(1, max_count)
    return list_monstre[alea]

#supprime un monstre de la base
def delete_monster(db, monstre):
    print("IN DELETE_MONSTER")
    db.delete_one({"_id", ObjectId(monstre)})

#verifie la santé d'un perso
def check_monstre(list_monstre, monstre):
    print("IN DEFAIE_MONSTRE")
    if monstre["PV"] <=0:
        pop_monster(list_monstre, monstre)
        score =score +1
        check_list_monstre(list_monstre)
        

def check_list_monstre(list_monstre):
    print("IN CHECK_LIST_MONSTER")
    if len(list_monstre) <1:
        game.you_win()
    
#retire un perso de l'equipe
def pop_monster(list_monstre, monstre):
    print("IN POP_monstre")
    print(f"degage {monstre}")
    list_monstre.pop(list_monstre.index(monstre))
