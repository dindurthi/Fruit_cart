import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruit"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO shopper(shopper_id,name,email,shop_pas) VALUES(1,'Steve Wozniak','wozniak@gmail.com','123')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email,shop_pas) VALUES(2,'Bjarne Stroustrup','strous@gmail.com','123')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email,shop_pas) VALUES(3,'Frances Allen','allen@gmail.com','123')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email,shop_pas) VALUES(4,'Bjarne Stroustrup','strous@gmail.com','123')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email,shop_pas) VALUES(5,'Jeff Bezos','bezos@gmail.com','123')")

mydb.commit()
print(mycursor.rowcount, "record inserted.")



  
    
                  

     
