import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruits"
)


mycursor = mydb.cursor()

#Write SQL to get number of retailers available in the system
mycursor.execute("select count(retailer_id) from retailer")
retailid=[row[0] for row in mycursor.fetchall()]
print("number of retailers available in the system are{}".format(retailid[0]))

#write SQL to get the shopper count for each retailer
mycursor.execute("select distinct retailer_id,count(shopper_id) from cart_order\
                 join retailer_store on cart_order.shop_id=retailer_store.store_id \
                 group by retailer_store.retailer_id")
for x in mycursor:
    print(x)


#Write SQL to get all shoppers count
mycursor.execute("select count(shopper_id) from shopper")
for x in mycursor:
    print(x)


#Write SQL to get the purchase amount for each retailer
mycursor.execute("select retailer_id,sum(total_amount) from cart_order join \
                 retailer_store on cart_order.shop_id=retailer_store.store_id \
                 group by retailer_store.retailer_id")
for x in mycursor:
    print(x)


#Write SQL to find top retailer based on number of purchases
mycursor.execute("select retailer_id,sum(total_amount) from cart_order join \
                 retailer_store on cart_order.shop_id=retailer_store.store_id \
                 group by retailer_store.retailer_id\
                  order by sum(total_amount) desc")
for x in mycursor:
    print(x)



