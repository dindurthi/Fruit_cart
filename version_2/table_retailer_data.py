import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruit"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(1,'Alan','Turing','turing@gmail.com','Wilmslow,UK','123',1000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(2,'Tim-Bererns','Lee','lee@gmail.com','London,UK','123',2000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(3,'Sergey','Brin','brin@gmail.com','Moscow,Russia','123',3000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(4,'Ken','Thompson','thompson@gmail.com','Louisiana,USA','123',4000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(5,'Larry','Page','page@gmail.com','Michigan,USA','123',5000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(6,'Donald','Knuth','knuth@gmail.com','Wisconsin,USA','123',6000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(7,'Grace','Hopper','hopper@gmail.com','New York,USA','123',7000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(8,'Dennis','Ritchie','ritchie@gmail.com','New York,USA','123',8000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(9,'James','Gosling','gosling@gmail.com','Alberta,Canada','123',9000)")
mycursor.execute("INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(10,'Michael','Stonebraker','stone@gmail.com','Massachusetts,USA','123','10000')")
mydb.commit()
print("table updated")



  
    
                  

     
