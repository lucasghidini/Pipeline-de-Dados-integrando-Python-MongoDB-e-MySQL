from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import requests


def connetct_mongodb(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client

def create_connect_db(client, db_name):
    db = client[db_name]
    return db

def create_connect_collection(db, coll_name):
    return db[coll_name]

def extract_api_data(url):
    response = requests.get(url)
    return response.json()

def insert_data(col, data):
    result = col.insert_many(data)
    n_docs_inseridos= len(result.inserted_ids)
    return n_docs_inseridos

if __name__ == "__main__":
    # carregando as variaveis de ambiente
    load_dotenv()
    db_passowrd = os.getenv('passorwd_mongodb')

    cliente = connetct_mongodb(f"mongodb+srv://lucashidini:{db_passowrd}@cluster-pipeline.2qeq7uu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Pipeline")
    db = create_connect_db(cliente, "db_produtos_desafio")
    col = create_connect_collection(db, "produtos" )
    data = extract_api_data('https://labdados.com/produtos')
    print(f"\nQuantidade de dados extraidos: {len(data)}")

    n_docs= insert_data(col, data)
    print(f"\nDocumentos inseridos na colecao: {n_docs}")

    cliente.close()