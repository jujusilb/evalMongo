from models import perso
from models import monstre
#from models.perso import team
import sys
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random

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
    monstrePnj =monstre.fetch_monster(list_monstre)
    personnage =None
    while len(team)>0:
        if personnage is None or perso.check_perso(team, personnage) == False: 
            personnage = perso.fetch_personnage(team)
        if personnage is None:
            game_over()
            return 0
        attaque(personnage, monstrePnj)
        tue =monstre.check_monster(list_monstre, monstrePnj)
        print("tue", tue)
        if tue:
            renew=monstre.check_list_monstre(list_monstre)
            #score =score +1
            if renew:
                list_monstre=monstre.about_monster(list_monstre)
                monstrePnj =monstre.fetch_monster(list_monstre)
        attaque(monstrePnj, personnage)
        mort =perso.check_perso(team, personnage)
        print ("mort = ", mort)
        print("len team", len(team))
        if(mort):
            perdu =perso.check_team(team)
            if(perdu):
                game_over()
        #tour(team, list_monstre, personnage, monstrePnj)v

def attaque(attaquant, defenseur):
    print("IN ATTAQUE")

    #print(f'{attaquant["name"]} :')
    #print(f'{attaquant["ATK"]} ATK')
    #print(f'{attaquant["DEF"]} DEF')
    #print(f'{attaquant["PV"]} PV')
    
    #print(f'\n{defenseur["name"]} :')
    #print(f'{defenseur["ATK"]} ATK')
    #print(f'{defenseur["DEF"]} DEF')
    #print(f'{defenseur["PV"]} PV')

    coup =attaquant["ATK"]-defenseur["DEF"]
    print("coup", coup  )
    if coup >=0:
        defenseur["PV"] -=coup
    print ("def-PV apres coup", defenseur["PV"])
    #print(f'(att-ATK {attaquant["ATK"]}) - (def-DEF {defenseur["DEF"]}) = coup{coup}')
    #print(f'(def-PV {defenseur["PV"]}) -= (coup {coup})')
    #print(f'{attaquant["name"]} envois une attaque a {defenseur["name"]} de {attaquant["ATK"]}pts')
    #print(f'{defenseur["name"]} dispose de {defenseur["DEF"]} pts de defense')
    #print(f'il lui reste donc {defenseur["PV"]}pts de vie')
        
def tour(team, list_monstre, personnage, monstrePnj):
    print("IN TOUR")
    attaque(personnage, monstrePnj)
    tue =monstre.check_monster(list_monstre, monstrePnj)
    print("tue", tue)
    if tue:
        monstre.pop_monster(list_monstre, monstrePnj)
        renew=monstre.check_list_monstre(list_monstre)
        #score =score +1
        if renew:
            list_monstre=monstre.about_monster(list_monstre)
            monstrePnj =monstre.fetch_monster(list_monstre)
    attaque(monstrePnj, personnage)
    mort =perso.check_perso(team, personnage)
    print ("mort = ", mort)
    print("len team", len(team))
    if(mort):
        perdu =perso.check_team(team)
        if(perdu):
            game_over()


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
    
#annonce la victoire d'un joueur
def you_win():
    print("IN YOU_WIN")
    print("YOU WIN ! a bientot !²")

#monstre.delete_monster(db, monstre)


#def attaque(attaquant, defenseur):
#    print("IN ATTAQUE")
#    coup =attaquant["ATK"]-defenseur["DEF"]
#    if coup >=0:
#        defenseur["PV"] = defenseur["PV"]-coup


#annonce la defaite d'un joueur
def game_over():
    print("IN GAME_OVER")
    print("Vous avez perdu, a bientot !")
    return 0

#recupere les meilleurs score 
def get_high_score(db):
    print("GET_HIGH_SCORE")
    return db.score.find()


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

