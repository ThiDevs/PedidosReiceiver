import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="produtos"
)

mycursor = mydb.cursor()
sql = "insert into pedidos values (default,%s,%s,%s,%s,%s,%s)"
val = ("John", "Highway 21","HotDog",'6','2018-05-05','c:\\')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")