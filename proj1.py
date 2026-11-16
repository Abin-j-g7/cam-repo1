import mysql.connector


connector = mysql.connector.connect(
host="localhost",
user = "root",
password = "Abin@2004",
database = "myDB"
)

cursor = connector.cursor()
# cursor.execute(""" CREATE TABLE Bills(sl_no INT primary key auto_increment,category varchar(30),amount_spend int )""")
# cursor.execute("insert into bills(category,amount_spend) values(%s,%s)",('food',1000))
# cursor.execute("insert into bills(category,amount_spend) values(%s,%s)",('grocery',2000))
# cursor.execute("insert into bills(category,amount_spend) values(%s,%s)",('shopping',3000))

cursor.execute("select sum(amount_spend) as toatal from bills")
result=cursor.fetchall()
print(result)

# connector.commit()
connector.close()

bills={''}