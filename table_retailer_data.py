import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  db="fruits"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO retailer(retailer_id,first_name,last_name,email,address,store_id)  VALUES(1,'Alan','Turing','turing@gmail.com','Wilmslow,UK',11)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(2,'Tim-Bererns','Lee','lee@gmail.com','London,UK',12)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(3,'Sergey','Brin','brin@gmail.com','Moscow,Russia',13)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(4,'Ken','Thompson','thompson@gmail.com','Louisiana,USA',14)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(5,'Larry','Page','page@gmail.com','Michigan,USA',15)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(6,'Donald','Knuth','knuth@gmail.com','Wisconsin,USA',16)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(7,'Grace','Hopper','hopper@gmail.com','New York,USA',17)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(8,'Dennis','Ritchie','ritchie@gmail.com','New York,USA',18)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(9,'James','Gosling','gosling@gmail.com','Alberta,Canada',19)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,store_id) VALUES(10,'Michael','Stonebraker','stone@gmail.com','Massachusetts,USA','110')")
mydb.commit()
print(mycursor.rowcount, "record inserted.")



  
    
                  

     
