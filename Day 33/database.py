import mysql.connector
import mysql

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="login"
        )
