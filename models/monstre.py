import random
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import file_games 
#from game import score
import db

##compte le nombre de monstre en base
#def count_monster(list_monstre):
#    ###print("IN COUNT_MONSTER")
#    return len(list_monstre)-1

def about_monster(list_monstre):
    ###print("IN ABOUT_MONSTRE")
    new_monsters = get_list_monster(db.get_database())
    list_monstre.extend([m.copy() for m in new_monsters])


#recupere la liste des monstre en database
def get_list_monster(db):
    ###print("IN GET_LIST_MONSTER")
    return list(db.monstres.find())
     


#recupere un monstre aleatoirement depuis list_monstre
def fetch_monster(list_monstre):
    ###print("IN FETCH_MONSTER")
    unSeulMonstre =random.choice(list_monstre)
    list_monstre.remove(unSeulMonstre)
    return unSeulMonstre

##supprime un monstre de la base
#def delete_monster(db, monstre):
#    ###print("IN DELETE_MONSTER")
#    db.delete_one({"_id", ObjectId(monstre)})

#verifie la santé d'un perso
def check_monster(list_monstre, monstrePNJ):
    #print("IN CHECK_MONSTER")
    
    if monstrePNJ["PV"] <=0:
       return True
    return False
        

def check_list_monstre(list_monstre):
    #print("IN CHECK_LIST_MONSTER")
    if len(list_monstre) <1:
        #print("letn listmonstre", len(list_monstre))
        return True
    return False
    
#retire un perso de l'equipe
def pop_monster(list_monstre, monstrePnj):
    ###print("IN POP_monstre")
    print(f"degage {monstrePnj["name"]}")
    list_monstre.remove(monstrePnj)
    print ("len list_monstre", len(list_monstre))
    #list_monstre.remove(list_monstre.index(monstrePnj))

