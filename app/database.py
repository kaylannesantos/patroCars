import os
import psycopg2

def get_db_connection():
    database_url = os.getenv("postgresql://userpostgres:hBK90sYkdDFXdFEYjsHfuGC2KQzuA3OF@dpg-cskm3jm8ii6s73ftdvtg-a.ohio-postgres.render.com/patrocars_oxal")
    banco = psycopg2.connect(database_url)
    return banco


"""
def get_db_connection():
    banco = psycopg2.connect(dbname='patrocars',user='postgres',password='123',host='localhost',port='5432')
    #banco = psycopg2.connect("dbname='patrocars' user=postgres password='123' host=localhost port=5432")

    return banco
"""