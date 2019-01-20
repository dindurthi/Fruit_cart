import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE fruits")
