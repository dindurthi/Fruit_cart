import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE fruit")
