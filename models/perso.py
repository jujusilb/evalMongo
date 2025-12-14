from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random
import file_games

#affiche les perso et creer une equipe
def about_perso(db, team):
    print("IN PERSO")
    nbperso=1
    list_perso =get_list_perso(db)
    team =create_team(list_perso, team, nbperso)

#affiche l'equipê
def show_team(team):
    print("IN SHOW_TEAM")
    print("VOICI L'EQUIPE")
    for item in team:
        print(item)


def show_perso(list_perso, nb):
    print("IN SHOW_PERSO")
    for item in list_perso:
        print(f"'Nom :{item['name']}, Defense :{item['DEF']}, Attaque :{item['ATK']}, Points de vie :{item['PV']}")

#recupere la liste des perso en base
def get_list_perso(db):
    print("IN GET_LIST_PERSO")
    return list(db.persos.find())

def fetch_personnage(team):
    print("IN FETCH_PERSONNAGE")
    return team[0]

#verifie si un perso est disponible
def check_array(list_perso, string):
    print("IN CHECK_ARRAY")
    for item in list_perso:
        if string == item["name"]:
            return True
    return False
     
#recupere le perso a partir de son nom
def get_dico_in_array(list_perso, chosen): # ???
    print("IN GET_DICO_IN_ARRAY - ln 79")
    for item in list_perso:
        if chosen ==item["name"]:
            return item
        

#retire un perso de l'equipe
def pop_perso(team, perso):
    print("IN POP_PERSO")
    team.pop(team.index(perso))

#verifie la santé d'un perso
def check_perso(team, personnage):
    print("IN DEFAIE_PËRSO")
    if personnage["PV"] <=0:
        pop_perso(team, personnage)

nbperso=1
perso_choisi =""
#créé l'equipe      
def create_team(list_perso, team, nbperso):
    print("IN CREATE_TEAM")
    while len(team) < 3:
        show_perso(list_perso, nbperso)
        temp =get_choice_perso(nbperso)
        perso_choisi =check_exists(list_perso, temp, nbperso, team)
        add_selection_in_team(list_perso, team, perso_choisi)
        nbperso =nbperso    +1
    show_team(team)
    return team

#recupere le choix d'un perso par le joueur
def get_choice_perso(nbperso):
    print("IN GET_CHOICE_PERSO")
    string =input(f"choisissez un personnage {nbperso} :")
    return string



#boucle tant que le perso n'existe pas
def check_exists(list_perso,string, perso, team):
    print("IN CHECK_EXISTS")
    boolean =check_array(list_perso, string)  # ??
    while not boolean: 
        string = get_choice_perso(perso)
    return string

#ajoute un perso a l'equipe
def add_selection_in_team(list_perso, team, chosen):
    print("IN ADD_SELECTION_IN_TEAM")
    personnage =get_dico_in_array(list_perso, chosen)
    team.append(personnage)
    list_perso.pop(list_perso.index(personnage))

#retire un perso de l'equipe
def pop_perso(team, personnage):
    print("IN POP_PERSO")
    for i, item in enumerate(team):
        if item["name"] == personnage["name"]:
            team.pop(i)
            break 
    #team.remove(team.index(personnage))

#verifie la saZnté d'un perso
def check_perso(team, personnage):
    print("IN DEFAIE_PËRSO")
    if personnage["PV"] <=0:
        print(f"farewell {personnage["name"]}")
        pop_perso(team, personnage)
        return True
    return False

##verifie si l'equipe n'est pas vide
#def check_team(team):
#    print("IN CHECK_TEAM")
#    if len(team) == 0:
#        file_games.game_over()


       