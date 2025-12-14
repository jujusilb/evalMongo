
##compte le nombre de monstre en base
#def count_monster(db):
#    ###print("IN COUNT_MONSTER")
#    return db.monstres.count_documents({})

##recupere un monstre aleatoirement depuis la base
#def fetch_monster(db):
#    ###print("IN FETCH_MONSTER")
#    max_count =count_monster(db)
#    alea =random.randint(1, max_count)
#    return db.monstres.find({"_id": ObjectId(alea)})
#