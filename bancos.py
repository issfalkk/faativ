#esse arquivo é responsável por criar/conectar o banco de dados

from sqlalchemy import create_engine, URL
#importamos do arquivo classes a Base
from classes import Base 
#imports pro mysql
import os
from dotenv import load_dotenv


def conectar_sqlite():
    #isso aqui cria o banco de dados Atelie
    engine = create_engine("sqlite:///atelie.db")

    # configuração para criar o arquivo de banco de dados
    Base.metadata.create_all(engine)

    return engine

def conectar_mysql():
    #isso aqui cria uma conexão com o banco de dados Atelie criado no mysql
    # ler o arquivo .env
    load_dotenv()

    # buscando as variáveis de ambiente
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    # definição do banco de dados
    engine = create_engine(
        URL.create(
            drivername="mysql+pymysql",
            username=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            database=MYSQL_DATABASE
        )
    ) #o engine esta diferente do exemplo do professor, pois estava dando erro de interpretação do URL

    # configuração para criar o arquivo de banco de dados
    Base.metadata.create_all(engine)

    return engine