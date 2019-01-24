import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruit"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(1000,1,'Alan Fruits','Wilmslow')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(2000,2,'Lee Fruits','London')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(3000,3,'Brin Fruits','Moscow')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(4000,4,'Ken Fruits','Louisiana')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(5000,5,'Larry Fruits','Michigan')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(6000,6,'Donald Fruits','Wisconsin')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(7000,7,'Grace Fruits','New York')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(8000,8,'Dennis Fruits','New York')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(9000,9,'Golsing Fruits','Alberta')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(10000,10,'Michael Fruits','Massachusetts')")
mydb.commit()
print("Table updated")



  
    
                  

     
