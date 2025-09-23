import polars as pl
from pymongo import MongoClient
from time import time




if __name__ == "__main__":
    print("Starting...")
    client = MongoClient("mongodb://localhost:27017/")
    db = client.mydb
    collection = db.mycollection
    file_path = r"C:\Users\adm\Desktop\DataSets\customers-2000000.csv"
    start = time()
    df = pl.read_csv(file_path)
    print(df.shape)
    
    records = df.to_dicts()
    collection.insert_many(records)
    end = time()
    delta = end - start
    print(f"Time: {delta}")