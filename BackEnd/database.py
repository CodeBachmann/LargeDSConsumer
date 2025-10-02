from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/bigstore")

def get_db():
    db = client["bigstore"]
    
    yield db
