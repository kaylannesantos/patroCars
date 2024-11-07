import psycopg2
import os

def get_db_connection():
    database_url = os.getenv("postgresql://userpostgre:lfxFlRe6L2bYmEA5jnwGBteTVX3M4vqy@dpg-csmamfjqf0us73fvbs10-a.ohio-postgres.render.com/patrocars_z8n0")
    banco = psycopg2.connect(database_url)
    return banco

"""
def get_db_connection():
    banco = psycopg2.connect(dbname='patrocars',user='postgres',password='123',host='localhost',port='5432')
    #banco = psycopg2.connect("dbname='patrocars' user=postgres password='123' host=localhost port=5432")

    return banco
"""
