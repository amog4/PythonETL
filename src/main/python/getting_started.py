import mysql.connector as mc
from mysql.connector import errorcode as ec

user = "retail_user"
password = "amogh"
host ="localhost"
db = "retail"

"""connection = mc.connect(user=user,
                        password=password,
                        host=host,
                        port=3307,
                        database = db)


connection.close()"""


import psycopg2

conn = psycopg2.connect("dbname='retail_dw' user='postgres' host='localhost' port=5433 password='amogh'")

conn.close()