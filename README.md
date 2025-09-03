# Pipeline ETL(extract, transform, load) integrando Python + MongoDB + MySQL
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📖 Sobre o Projeto
Nesse projeto usei a api publica [labdados.com](labdados.com/produtos) para obter dados fictícios sobre produtos.

Também utilizei o MongoDB para salvar os dados brutos.

Após salvar os dados no banco de dados, usei o Python e suas bibliotecas para tratar os dados de uma maneira que pudessem ser reutilizados facilmente.

Depois de tratar os dados, decidi usar o MySQL para salvá-los de forma tabular, facilitando ainda mais a visualização e utilização dos dados.

## Fluxo do Projeto


## Como execultar o projeto
### 1. Pré-requisitos
-   Python 3.8 ou superior
-   Um servidor MySQL 8.0 ou superior (local ou na nuvem)
-   Um Banco de dados no MongoDB(atlas)

Clone o repositório e instale as dependências:
```bash
git clone https://github.com/lucasghidini/Pipeline-de-Dados-integrando-Python-MongoDB-e-MySQL.git

cd Pipeline-de-Dados-integrando-Python-MongoDB-e-MySQL
```
Crie um arquivo com o nome 'requirements.txt' contendo:
```bash
python
pymongo
mysql-connector-python
pandas
```
e instale com pip
```
pip instal -r requirements.txt
```
É nessesario um arquivo .env com variaveis de ambientes para o projeto funcionar, crie um com as seguintes informações:
```
passorwd_mongodb = senha do seu database do MongoDB

DB_USER = user do MySQL
DB_PASSWORD = senha usada
DB_HOST = host do MySQL
DB_NAME = nome do database

```

feito por Lucas Ghidini