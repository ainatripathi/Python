import mysql.connector
import mysql

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="login"
        )

def create_db():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )
    cursor=conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS login")
    conn.close()

    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="login"
        )
    cursor=conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS data(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(50) NOT NULL
)
""")
    conn.close()
