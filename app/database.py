import os
import psycopg2

def get_db_connection():
    banco = psycopg2.connect(
        dbname= os.getenv("patrocars_jvgt"),
        user= os.getenv("patrocars_jvgt_user"),
        password= os.getenv("3SvpJJyK5PauzVt5UPhjFywPriLJUPPY"),
        host= os.getenv("dpg-cskbfprtq21c73dlcqmg-a"),
        port= os.getenv("5432")
        )
    #banco = psycopg2.connect(dbname='patrocars',user='postgres',password='123',host='localhost',port='5432')
    #banco = psycopg2.connect("dbname='patrocars' user=postgres password='123' host=localhost port=5432")
    return banco