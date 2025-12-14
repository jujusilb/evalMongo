from pymongo import MongoClient

#se connecte a la db
def get_database():
    ###print("IN GET_DATABASE")
    # URI local : "mongodb://localhost:27017"
    # Ou URI Atlas : "mongodb+srv://<user>:<password>@cluster0.mongodb.net/"
    #client = MongoClient("mongodb://127.0.0.1:27017")
    client = MongoClient("mongodb+srv://jujusilb:Gaspesie@cluster0.revmtu2.mongodb.net/?appName=Cluster0")
    db = client["evalMongo"]  # Base de données "todo_db"
    return db   