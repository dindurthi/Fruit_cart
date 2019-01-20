import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  db="fruits"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO shopper(shopper_id,name,email) VALUES(21,'Steve Wozniak','wozniak@gmail.com')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email) VALUES(22,'Bjarne Stroustrup','strous@gmail.com')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email) VALUES(23,'Frances Allen','allen@gmail.com')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email) VALUES(24,'Bjarne Stroustrup','strous@gmail.com')")
mycursor.execute("INSERT INTO shopper(shopper_id,name,email) VALUES(25,'Jeff Bezos','bezos@gmail.com')")

mydb.commit()
print(mycursor.rowcount, "record inserted.")



  
    
                  

     
