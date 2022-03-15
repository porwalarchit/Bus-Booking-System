import sqlite3

conn = sqlite3.Connection('test.db')
cur = conn.cursor()

cur.execute("Create Table If Not Exists Friends (Id int ,Name varchar(50))")
cur.execute("Insert into Friends Values(12,'Adarsh')")
cur.execute("Insert into Friends Values(32,'Vivek')")

cur.execute("Select * from Friends")
print(cur.fetchall())

conn.commit()
print("Records created successfully")
conn.close()