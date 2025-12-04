import random


#compte le nombre de monstre en base
def count_monster(list_monstre):
    print("IN COUNT_MONSTER")
    return len(list_monstre)

def about_monster(db):
    print("IN ABOUT_MONSTRE")
    list_monstre =get_list_monster(db)
    return fetch_monster(list_monstre)


#recupere la liste des monstre en database
def get_list_monster(db):
    print("IN GET_LIST_MONSTER")
    return list(db.monstre.find())
     


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
        pop_monstre(list_monstre, monstre)
        check_list_monstre(list_monstre)
    
    
#retire un perso de l'equipe
def pop_monster(list_monstre, monstre):
    print("IN POP_monstre")
    list_monstre.pop(list_monstre.index(monstre))
