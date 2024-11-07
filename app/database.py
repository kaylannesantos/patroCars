import psycopg2
import os

def get_db_connection():
    database_url = os.getenv("DATABASE_URL")  # configure a variavel de ambiente como DATABASE_URL
    if not database_url:
        raise ValueError("Conexão com banco de dados não estabelecida!.")
    banco = psycopg2.connect(database_url)
    return banco

"""
def get_db_connection():
    banco = psycopg2.connect(dbname='patrocars',user='postgres',password='123',host='localhost',port='5432')
    #banco = psycopg2.connect("dbname='patrocars' user=postgres password='123' host=localhost port=5432")

    return banco
"""
