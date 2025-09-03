from extract_and_save_data import connetct_mongodb, create_connect_db, create_connect_collection
import pandas as pd
from dotenv import load_dotenv
import os
import requests


def visualize_colletion(col):
    for doc in col.find():
        print(doc)

def rename_column(col, col_name, new_name):
    col.update_many({}, {'$rename': {col_name: new_name}})

def select_category(col, category):
    query = {'Categoria do Produto': f'{category}'}
    
    lista_categoria = []
    for doc in col.find(query):
        lista_categoria.append(doc)
    return lista_categoria
    

def make_regex(col, regex):
    query = {'Data da Compra': {'$regex': f'{regex}'}}

    lista_regex=[]
    for doc in col.find(query):
        lista_regex.append(doc)
    return lista_regex

def create_dataframe(lista):
    df = pd.DataFrame(lista)
    return df

def format_date(df):
    df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format= '%d/%m/%Y')
    df['Data da Compra'] = df['Data da Compra'].dt.strftime('%Y-%m-%d')

def save_csv(df, patch):
    df.to_csv(patch, index=False)
    print(f'Arquivo {patch} salvo com sucesso!')

if __name__ == '__main__':
    # carregando as variaveis de ambiente
    load_dotenv()
    db_passowrd = os.getenv('passorwd_mongodb')

    # estabelecendo a conexão e recuperando os dados do MongoDB
    cliente = connetct_mongodb(f"mongodb+srv://lucashidini:{db_passowrd}@cluster-pipeline.2qeq7uu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Pipeline")
    db = create_connect_db(cliente, "db_produtos_desafio")
    col = create_connect_collection(db, "produtos" )

    # visualizando os dados da coleção
    #visualize_colletion(col)

    #renomeando as colunas latiude e longitude
    rename_column(col, "lat", "Latitude")
    rename_column(col, "lon", "Longitude")


    #salvando os dados da categoria livros
    lst_livros = select_category(col, 'livros')
    df_livros = create_dataframe(lst_livros)
    format_date(df_livros)
    save_csv(df_livros, r'C:\Users\Lucas\Desktop\Alura\Trilha data science\MongoDB, Python\data\livros.csv')

    # salvando dados de vendas a partir de 2021
    lst_produtos = make_regex(col, '/202[1-9]')
    df_produtos = create_dataframe(lst_produtos)
    format_date(df_produtos)
    save_csv(df_produtos, r'C:\Users\Lucas\Desktop\Alura\Trilha data science\MongoDB, Python\data\vendas_2021.csv')

    cliente.close()