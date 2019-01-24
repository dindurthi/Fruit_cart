import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruit"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE retailer (retailer_id INT,first_name VARCHAR(255),last_name VARCHAR(255),email VARCHAR(255),address VARCHAR(255),retailer_pass VARCHAR(255),store_id INT,PRIMARY KEY(retailer_id))")
mycursor.execute("CREATE TABLE shopper(shopper_id INT,name VARCHAR(255),email VARCHAR(255),shop_pas VARCHAR(255),PRIMARY KEY(shopper_id))")
mycursor.execute("CREATE TABLE retailer_cart (product_id INT,store_id INT,item VARCHAR(255),quantity INT,price INT,PRIMARY KEY(product_id))")
mycursor.execute("CREATE TABLE retailer_store (store_id INT,retailer_id INT,store_name VARCHAR(255), location VARCHAR(255),PRIMARY KEY(store_id))")
mycursor.execute("CREATE TABLE cart_order (order_id INT AUTO_INCREMENT,shop_id INT,shopper_id INT,shopper_name VARCHAR(255),total_amount INT,PRIMARY KEY(order_id))")
mycursor.execute("CREATE TABLE order_details(order_details_id INT AUTO_INCREMENT,order_id INT,shop_id INT,product_id INT,product_name VARCHAR(255),quantity INT,price INT,PRIMARY KEY(order_details_id))")




