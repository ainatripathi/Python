import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )

if conn.is_connected():
    print("Connected to MySQL Server")

conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )

cursor=conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mycollege")
print("Database created successfully")

conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )

cursor=conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(100),
               marks INT
               )
               """)

print("Table Created successfully.")

conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )

cursor=conn.cursor()
sql="INSERT INTO student (name,marks) VALUES(%s,%s)"
values=[("Ravi",85),("Priya",90),("Ashish",75)]
cursor.executemany(sql,values)
conn.commit()
print(cursor.rowcount," records inserted.")
conn.close()

conn.close()
