from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb://jesusnava:12nomelase.com@ac-z7hma36-shard-00-00.gnqenap.mongodb.net:27017,ac-z7hma36-shard-00-01.gnqenap.mongodb.net:27017,ac-z7hma36-shard-00-02.gnqenap.mongodb.net:27017/?ssl=true&replicaSet=atlas-112dvm-shard-0&authSource=admin&retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de Conexion con la bdd')
    return db