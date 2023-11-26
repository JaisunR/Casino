import pymongo
import certifi


class MongoDB:
    def __init__(self, db_name, collection_name) -> None:
        self.client = self.client = pymongo.MongoClient(
            "mongodb+srv://Jacob2:xOecJJ12zJSATm1o@cluster0.hlc3bi6.mongodb.net/?retryWrites=true&w=majority",
            tlsCAFile=certifi.where())
        self.db = self.get_create_database(db_name)
        self.collection = self.get_create_collection(collection_name)

    def get_create_database(self, db_name):
        if db_name not in self.client.list_database_names():
            new_db = self.client[db_name]
            print(f"Database '{db_name}' created.")
        else:
            new_db = self.client[db_name]
            print(f"Database '{db_name}' already exists.")
        return new_db

    def get_create_collection(self, collection_name):
        if collection_name not in self.db.list_collection_names():
            new_collection = self.db[collection_name]
            print(f"Collection '{collection_name}' created.")
        else:
            new_collection = self.db[collection_name]
            print(f"Collection '{collection_name}' already exists.")
        self.collection = new_collection
        return new_collection


user = MongoDB(db_name="casino", collection_name="user").collection
transaction = MongoDB(db_name="casino", collection_name="transaction").collection
balance = MongoDB(db_name="casino", collection_name="balance").collection
game_history = MongoDB(db_name="casino", collection_name="game_history").collection
