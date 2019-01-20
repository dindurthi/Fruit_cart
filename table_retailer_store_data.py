import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  db="fruits"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(11,1,'Alan Fruits','Wilmslow')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(12,2,'Lee Fruits','London')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(13,3,'Brin Fruits','Moscow')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(14,4,'Ken Fruits','Louisiana')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(15,5,'Larry Fruits','Michigan')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(16,6,'Donald Fruits','Wisconsin')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(17,7,'Grace Fruits','New York')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(18,8,'Dennis Fruits','New York')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(19,9,'Golsing Fruits','Alberta')")
mycursor.execute("INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(110,10,'Michael Fruits','Massachusetts')")
mydb.commit()
print(mycursor.rowcount, "record inserted.")



  
    
                  

     
