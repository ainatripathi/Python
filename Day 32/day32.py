import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )

cursor=conn.cursor()
cursor.execute("SELECT * FROM student")

rows=cursor.fetchall()

for row in rows:
    print(row)

conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )

cursor=conn.cursor()
sql="UPDATE student SET marks=%s WHERE name=%s"
val=(95,"Ravi")
cursor.execute(sql,val)
conn.commit()
print(cursor.rowcount," record(s) updated.")
conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )

cursor=conn.cursor()
sql="DELETE FROM student WHERE name=%s"
val=("Ashish",)
cursor.execute(sql,val)
conn.commit()
print(cursor.rowcount," record(s) deleted.")
conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )

cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS student")
print("Table dropped successsfully.")
conn.close()

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="guiform"
    )

cursor.execute("""
               CREATE TABLE IF NOT EXISTS students(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(100),
               marks INT
               )
               """)
