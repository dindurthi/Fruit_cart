import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruit"
)


mycursor = mydb.cursor()
#mycursor.execute("UPDATE retailer_cart set price=2 where prod")
mycursor.execute("select * from retailer_cart")
#mydb.commit()
for x in mycursor:
  print(x)


                 
  
