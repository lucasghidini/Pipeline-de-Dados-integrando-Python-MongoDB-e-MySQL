import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

class save_data_mysql():
    def __init__(self, db_config):
        self.db_config = db_config

    
    def connect_mysql(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            print('Sucesso: Conexão com banco de dados realizada')
            return conn
        except mysql.connector.Error as e:
            print(f'Erro ao conenctar com o MySQL: {e}')
            return None

    def create_cursor(self, conn):
        cursor = conn.cursor()
        return cursor
    
    def create_database(self, cursor, db_name):
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}') 
        print(f'Sucesso: Banco de dados {db_name} criado ou já existe.')
    
    def show_databases(self, cursor):
        cursor.execute('SHOW DATABASES')
        for x in cursor:
            print(x)
    
    def create_product_table(self, cursor, db_name, tb_name):
        cursor.execute(f'''
        CREATE TABLE {db_name}.{tb_name}(
                id VARCHAR(100),
                Produto VARCHAR(100),
                Categoria_Produto VARCHAR(100),
                Preco FLOAT(10,2),
                Frete FLOAT(10,2),
                Data_Compra DATE,
                Vendedor VARCHAR(100),
                Local_Compra VARCHAR(100),
                Avaliacao_Compra INT,
                Tipo_Pagamento VARCHAR(100),
                Qntd_Parcelas INT,
                Latitude FLOAT(10,2),
                Longitude FLOAT(10,2),
                
                PRIMARY KEY (id));
        ''')
        print(f'Sucesso: Tabela {tb_name} criada.')

    def show_tables(self, cursor, db_name):
        cursor.execute(f'USE {db_name}')    
        cursor.execute(f'SHOW TABLES')
        for x in cursor:
            print(x)
    
    def read_csv(self, patch):
        df = pd.read_csv(patch)
        return df
    
    def add_products_data(self, conn, cursor, df, db_name, tb_name):
        lista = [tuple(row) for i, row in df.iterrows()]
        sql = f'INSERT INTO {db_name}.{tb_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'

        cursor.executemany(sql, lista)
        print(f'Sucesso: {cursor.rowcount} Dados inseridos na tabela {tb_name}.')
        conn.commit()

def main():
    db_handler = save_data_mysql(db_config)
    conn = db_handler.connect_mysql()
    
    if conn is None:
        print('Erro: Não foi possível conectar ao banco de dados.')
        return
    
    cursor = db_handler.create_cursor(conn)

    try:
        db_name = os.getenv('DB_NAME')
        tb_name = 'tb_produtos'
        csv_path = r'C:\Users\Lucas\Desktop\Alura\Trilha data science\MongoDB, Python\data\tabela_produtos.csv'

        db_handler.create_database(cursor, db_name)  
        db_handler.create_product_table(cursor, db_name, tb_name)

        df = db_handler.read_csv(csv_path)

        db_handler.add_products_data(conn, cursor, df, db_name, tb_name)

    except mysql.connector.Error as e:
        print(f'Erro ao executar operações no MySQL: {e}')

    finally:
        cursor.close()
        conn.close()
        print('Conexão com o banco de dados encerrada.')    

if __name__ == '__main__':
    main()