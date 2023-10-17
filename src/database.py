from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os


class Database:
    def __init__(self):
        load_dotenv()
        self.products = self.connect()

    def connect(self):
        client = MongoClient(os.getenv("DB_URI"))
        db = client["dados"]
        return db.products

    def search(self, productName: str) -> list | None:
        searchResult = []
        for product in self.products.find():
            if product['title'].lower().find(productName.lower()) != -1:
                searchResult.append(product)
        return searchResult
    def insert(self, data: dict) -> dict | None:
        query = {'title': data['title']}
        result = self.products.find_one(query, sort=[('date', -1)])
        if result is None:
            self.products.insert_one(data)
            return data
        elif result['price'] > data['price'] or result['price'] < data['price']:
            self.products.insert_one(data)
            return data
        else:
            return None
