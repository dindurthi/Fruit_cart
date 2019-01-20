import mysql.connector
from itertools import combinations
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  db="fruits"
)
#connect to the database
mycursor = mydb.cursor()
mycursor.execute("select shopper_id from shopper")
display=[row[0] for row in mycursor.fetchall()]
for x in display:
  print(x)
# select shopper id from the system
shopperid=input("enter your shopper id: ")
quert="select name from shopper where shopper_id='%s'"
mycursor.execute(quert, (int(shopperid),))
shoppername=[row[0] for row in mycursor.fetchall()]


mycursor.execute("select * from retailer_cart")
#select the products in the cart
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#display the products in the cart

storeid=input("enter store id from the list: ")
#select the store from which you want to shop
mycursor.execute("select store_id from retailer_store")
store_user = [row[0] for row in mycursor.fetchall()]
flag=0
for x in store_user:
        if x==int(storeid):
          print("valid selection")
          flag=1
          #check whether the selection is valid
if flag==1:
  sql_query2="select * from retailer_cart where store_id='%s'"
  mycursor.execute(sql_query2, (int(storeid),))
  display1=mycursor.fetchall()
  for x in display1:
    print(x)
  for i in range(len(display1)):
    print("{}.{}".format(i,display1[i][2]))
else:
  print("invalid selection")


arr=[1,2,3,4,5,6,7,8,9] #each fruit represented as number
r=3
# number of combinations
combi=list(combinations(arr,r))
print(combi)
#show the number of combinations possible with the fruits
print("enter a selection from the list")
se=[int(x) for x in input("enter numbers seperated by spaces: ").split()]
sel=tuple(se)

for i in range(len(combi)):
         if sel==combi[i]:
               print("valid selection")
              #check whether the selection is valid
sql_query3="select product_id from retailer_cart where store_id='%s'"
mycursor.execute(sql_query3, (int(storeid),))
productid= [row[0] for row in mycursor.fetchall()]
#select appropriate price,item and quantity from the retailer_cart
for x in productid:
  if x%10==sel[0]:
    prodid1=x
    sql_query4="select price from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query4, (int(x),))
    a=[row[0] for row in mycursor.fetchall()]
    sql_query5="select item from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query5, (int(x),))
    a1=[row[0] for row in mycursor.fetchall()]
    sql_query5="select quantity from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query5, (int(x),))
    n1=[row[0] for row in mycursor.fetchall()]
  if x%10==sel[1]:
    prodid2=x
    sql_query4="select price from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query4, (int(x),))
    b=[row[0] for row in mycursor.fetchall()]
    sql_query5="select item from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query5, (int(x),))
    b1=[row[0] for row in mycursor.fetchall()]
    sql_query5="select quantity from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query5, (int(x),))
    n2=[row[0] for row in mycursor.fetchall()]
  if x%10==sel[2]:
    prodid3=x
    sql_query4="select price from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query4, (int(x),))
    c=[row[0] for row in mycursor.fetchall()]
    sql_query5="select item from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query5, (int(x),))
    c1=[row[0] for row in mycursor.fetchall()]
    sql_query5="select quantity from retailer_cart where product_id='%s'"
    mycursor.execute(sql_query5, (int(x),))
    n3=[row[0] for row in mycursor.fetchall()]
r1=n1[0]#quantity of fruit 1 in the retailer cart
r2=n2[0]# quanity of fruit 2 in the retailer cart
r3=n3[0]# quantity of fruit 3 in the retailer cart
x=a[0] #price of fruit 1
y=b[0] #price of fruit 2
z=c[0] #price of fruit 3
x1=a1[0] #fruit 1
y1=b1[0]# fruit 2
z1=c1[0]# fruit 3

for i in range(1,r1):
        for j in range(1,r2):
            for k in range(1,r3):
                sumnum=x*i+y*j+z*k
                if(sumnum==100.0):
                    print('you can select {},{} {},{} {},{}'.format(i,x1,j,y1,k,z1))  #print all the possible combinations for the given condition
                  
print('choose the combination of fruits you want to enter')
selection=[int(x) for x in input("enter numbers seperated by spaces").split()] #shopper selects the desired combination
quan1=selection[0] #quantity of fruit  selected by the user
price1=quan1*x    # quantity * price 
quan2=selection[1]
price2=quan2*y
quan3=selection[2]
price3=quan3*z

if(x*selection[0]+y*selection[1]+z*selection[2]==100):
    print("valid selection")#check for valid data 
    quer1="INSERT INTO cart_order(shop_id,shopper_id,shopper_name,total_amount)VALUES(%s,%s,%s,%s)"
    mycursor.execute(quer1,(int(storeid),int(shopperid),shoppername[0],(int(100))))     #insert row in cart_order
    mydb.commit()
    mycursor.execute("select order_id from cart_order order by order_id desc limit 1")
    orderid=[row[0] for row in mycursor.fetchall()]
    quer2="INSERT INTO order_details(order_id,shop_id,product_id,product_name,quantity,price)VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(quer2,(int(orderid[0]),int(storeid),int(prodid1),x1,int(quan1),(int(price1))))
    mycursor.execute(quer2,(int(orderid[0]),int(storeid),int(prodid2),y1,int(quan2),(int(price2))))
    mycursor.execute(quer2,(int(orderid[0]),int(storeid),int(prodid3),z1,int(quan3),(int(price3))))  
    mydb.commit()
    #insert rows in order_details
    upquan1=r1-quan1
    upquan2=r2-quan2
    upquan3=r3-quan3
    quer3="UPDATE retailer_cart SET quantity='%s' where product_id='%s'"  
    mycursor.execute(quer3,(int(upquan1),int(prodid1)))
    mycursor.execute(quer3,(int(upquan2),int(prodid2)))
    mycursor.execute(quer3,(int(upquan3),int(prodid3)))
    #update quantities in the retailer_cart
    mydb.commit()
    print("tables updated")

