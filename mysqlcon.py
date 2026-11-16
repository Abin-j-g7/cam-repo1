import mysql.connector

connector = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Abin@2004",
    database = "myDB"
)

cursor = connector.cursor()
# cursor.execute(""" CREATE TABLE CAMO (ID INT PRIMARY KEY,NAME VARCHAR(30),DESIGNATION VARCHAR(30))""")
# cursor.execute("insert into camo values(%s,%s,%s)",(1,"abin","data Science"))
# cursor.execute("insert into camo values(%s,%s,%s)",(2,"chris","data science"))
# cursor.execute("insert into camo values(%s,%s,%s)",(3,"sid","fullstack"))
# connector.commit()
cursor.execute("UPDATE CAMO SET NAME = 'ABIN k b' WHERE ID = 1")
connector.commit()
cursor.execute("SELECT * FROM CAMO")
for i in cursor.fetchall():
    print(i)

connector.close()