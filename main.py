import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="farmaciamaromba"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM funcionario")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

