import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  db="fruits"
)


mycursor = mydb.cursor()

#Write SQL to get number of retailers available in the system
mycursor.execute("select count(retailer_id) from retailer")
retailid=[row[0] for row in mycursor.fetchall()]
print("number of retailers available in the system are{}".format(retailid[0]))

#write SQL to get the shopper count for each retailer
mycursor.execute("select distinct retailer_id,count(shopper_id) from order_details\
              join cart_order on order_details.order_id=cart_order.order_id \
              join retailer_store on order_details.shop_id=retailer_store.store_id \
              group by order_details.shop_id")
for x in mycursor:
    print(x)

#Write SQL to get all shoppers count
mycursor.execute("select count(shopper_id) from shopper")
for x in mycursor:
    print(x)


#Write SQL to get the purchase amount for each retailer
mycursor.execute("select shop_id,sum(price) from order_details group by shop_id")
for x in mycursor:
    print(x)
    
mycursor.execute("select retailer_id,first_name,last_name from retailer where retailer_id=(select retailer_id from retailer_store where store_id=(select shop_id from order_details group by shop_id limit 1))")
for x in mycursor:
    print(x)

