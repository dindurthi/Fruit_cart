import mysql.connector
from itertools import combinations
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Indu@5812",
  db="fruit"
)
mycursor = mydb.cursor()
identity=input("Are you a shopper or retailer? \n Enter r for retailer and s for shopper ")
if(identity=='r'):
  print("welcome to retailer page")
  retailer_n=input("Are you a new retailer or existing retailer? \n Enter n for new retailer and e for existing ")
  if(retailer_n=='n'):
    ret_pas=input("Hello, welcome to the retailer page!\n enter the password given at the time of registration: ")
    if ret_pas=='123':
      print("Please enter the following information")
      ret_first_name=input("enter your first name")
      ret_last_name=input("enter last name")
      ret_email=input("enter email")
      ret_address=input("enter address")
      ret_password=input("enter the password you want to set")
      mycursor.execute("select retailer_id from retailer order by retailer_id desc limit 1")
      disp_retid=[row[0] for row in mycursor.fetchall()]
      ret_retid=int(disp_retid[0])+1
      ret_storeid=ret_retid*1000
      query1="INSERT INTO retailer (retailer_id,first_name,last_name,email,address,retailer_pass,store_id) VALUES(%s,%s,%s,%s,%s,%s,%s)"
      mycursor.execute(query1,(int(ret_retid),ret_first_name,ret_last_name,ret_email,ret_address,ret_password,(int(ret_storeid))))
      mydb.commit()
      ret_store_name=input("enter store name")
      ret_location=input("enter location")
      query2="INSERT INTO retailer_store (store_id,retailer_id,store_name,location)VALUES(%s,%s,%s,%s)"
      mycursor.execute(query2,(int(ret_storeid),int(ret_retid),ret_store_name,ret_location))
      mydb.commit()
      yn=input("Do you want to add items to your cart? enter y for yes and any key to exit")
      while(yn=='y'):
        query3="select * from retailer_cart where store_id='%s'"
        mycursor.execute(query3, (int(ret_storeid),))
        disp_retcart=mycursor.fetchall()
        if disp_retcart==[]:
          ret_prodid=ret_storeid+1
        else:
          query4="select product_id from retailer_cart where store_id='%s' order by product_id desc limit 1"
          mycursor.execute(query4, (int(ret_storeid),))
          disp_prodid=[row[0] for row in mycursor.fetchall()]
          ret_prodid=disp_prodid[0]+1
        ret_item=input("enter the name of the fruit")
        ret_quant=int(input("enter quantity"))
        ret_price=int(input("enter price"))
        query5="INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(%s,%s,%s,%s,%s)"
        mycursor.execute(query5,(int(ret_prodid),int(ret_storeid),ret_item,int(ret_quant),int(ret_price)))
        mydb.commit()
        print("Cart Updated")
        yn=input(" do you want to continue making changes? press y for yes, press any key to quit")
    else:
       print("Wrong password")
  if retailer_n=='e':
    ret_retid=input("enter retailer id")
    query6="select retailer_id from retailer where retailer_id='%s'"
    mycursor.execute(query6, (int(ret_retid),))
    disp_retid=[row[0] for row in mycursor.fetchall()]
    if int(ret_retid)==disp_retid[0]:
      ret_password=input("enter password")
      query7="select retailer_pass from retailer where retailer_id='%s'"
      mycursor.execute(query7, (int(ret_retid),))
      disp_pass=[row[0] for row in mycursor.fetchall()]
      if ret_password==disp_pass[0]:
        print("valid password\n Your Cart")
        query8="select store_id from retailer where retailer_id='%s'"
        mycursor.execute(query8, (int(ret_retid),))
        disp_storid=[row[0] for row in mycursor.fetchall()]
        query9="select * from retailer_cart where store_id='%s'"
        mycursor.execute(query9, (int(disp_storid[0]),))
        disp_retcart=mycursor.fetchall()
        for x in disp_retcart:
          print(x)
        yn=input("do you want to make any changes to your cart. Type y for yes or n for no")
        while(yn=='y'):
          print("Menu\n 1. enter 1 to change the price of the item")
          print("2. enter 2 to change the quantity of the item")
          print("3. enter 3 to add an item")
          print("4. enter 4 to delete an item")
          choice=input("enter choice: ")
          if choice=='1':
            ch_prodid=int(input("enter product id from the list"))
            ch_price=int(input("enter the price of the product"))
            query10="UPDATE retailer_cart set price='%s' where product_id='%s'"
            mycursor.execute(query10,(int(ch_price),int(ch_prodid)))
            mydb.commit()
            query11="select * from retailer_cart where product_id='%s'"
            mycursor.execute(query11, (int(ch_prodid),))
            display6=mycursor.fetchall()
            for x in display6:
              print(x)
            print("your cart has been updated")
            yn=input(" do you want to continue making changes? press y for yes, press any key to quit")
          elif choice=='2':
            ch_prodid=int(input("enter product id from the list"))
            ch_quant=int(input("enter the quantity of the product"))
            query12="UPDATE retailer_cart set quantity='%s' where product_id='%s'"
            mycursor.execute(query12,(int(ch_quant),int(ch_prodid)))
            mydb.commit()
            query13="select * from retailer_cart where product_id='%s'"
            mycursor.execute(query13, (int(ch_prodid),))
            display6=mycursor.fetchall()
            for x in display6:
              print(x)
            print("your cart has been updated")
            yn=input(" do you want to continue making changes? press y for yes, press any key to quit")
          elif choice=='3':
            query14="select product_id from retailer_cart where store_id='%s' order by product_id desc limit 1"
            mycursor.execute(query14, (int(disp_storid[0]),))
            disp_prod=[row[0] for row in mycursor.fetchall()]
            ch_prodid=disp_prod[0]+1
            ch_storeid=disp_storid[0]
            ch_item=input("enter the name of the fruit")
            ch_quant=int(input("enter quantity"))
            ch_price=int(input("enter price"))
            query15="INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(%s,%s,%s,%s,%s)"
            mycursor.execute(query15,(int(ch_prodid),int(ch_storeid),ch_item,int(ch_quant),int(ch_price)))
            mydb.commit()
            print("Cart Updated")
            yn=input(" do you want to continue making changes? press y for yes, press any key to quit")
          elif choice=='4':
            ch_prodid=int(input("enter the product id of the item you want to delete"))
            query19="delete from retailer_cart where product_id='%s'"
            mycursor.execute(query19,(int(ch_prodid),))
            mydb.commit()
            print("Cart Updated")
            yn=input(" do you want to continue making changes? press y for yes, press any key to quit")
          else:
            print("invalid choice")
elif(identity=='s'):
  print("Welcom to the shopper page")
  shopper_n=input("are you new to the cart? Enter n if new, 'e' for existing")
  if(shopper_n=='n'):
    mycursor.execute("select shopper_id from shopper order by shopper_id desc limit 1")
    disp_shopid=[row[0] for row in mycursor.fetchall()]
    sh_shopperid=disp_shopid[0]+1
    sh_name=input("enter your name")
    sh_mail=input("enter your email")
    sh_pass=input("enter the password u want to set")
    query20="INSERT INTO shopper(shopper_id,name,email,shop_pas) VALUES(%s,%s,%s,%s)"
    mycursor.execute(query20, (int(sh_shopperid),sh_name,sh_mail,sh_pass))
    mydb.commit()
  elif(shopper_n=='e'):
    print("Welcome back")
    sh_shopperid=int(input("enter shopper id"))
    query21="select shopper_id from shopper where shopper_id='%s'"
    mycursor.execute(query21, (int(sh_shopperid),))
    disp_shid=[row[0] for row in mycursor.fetchall()]
    if int(sh_shopperid)==disp_shid[0]:
      sh_password=input("enter password")
      query22="select shop_pas from shopper where shopper_id='%s'"
      mycursor.execute(query22, (int(sh_shopperid),))
      disp_shpas=[row[0] for row in mycursor.fetchall()]
      if sh_password==disp_shpas[0]:
        print("success")
        query23="select name from shopper where shopper_id='%s'"
        mycursor.execute(query23, (int(sh_shopperid),))
        disp_shoprname=[row[0] for row in mycursor.fetchall()]
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
        if flag==1:
          sql_query2="select * from retailer_cart where store_id='%s'"
          mycursor.execute(sql_query2, (int(storeid),))
          display1=mycursor.fetchall()
          for x in display1:
            print(x)
          arr=[]
          for i in range(len(display1)):
            arr.append(i+1)
            print("{}.{}".format(i+1,display1[i][2]))
        else:
          print("invalid selection")
        r=3
        combi=list(combinations(arr,r))
        print(combi)
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
          if x%1000==sel[0]:
            prodid1=x
            sql_query4="select price from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query4, (int(x),))
            a=[row[0] for row in mycursor.fetchall()]
            sql_query5="select item from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query5, (int(x),))
            a1=[row[0] for row in mycursor.fetchall()]
            sql_query6="select quantity from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query6, (int(x),))
            n1=[row[0] for row in mycursor.fetchall()]
          if x%1000==sel[1]:
            prodid2=x
            sql_query4="select price from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query4, (int(x),))
            b=[row[0] for row in mycursor.fetchall()]
            sql_query5="select item from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query5, (int(x),))
            b1=[row[0] for row in mycursor.fetchall()]
            sql_query6="select quantity from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query6, (int(x),))
            n2=[row[0] for row in mycursor.fetchall()]
          if x%1000==sel[2]:
            prodid3=x
            sql_query4="select price from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query4, (int(x),))
            c=[row[0] for row in mycursor.fetchall()]
            sql_query5="select item from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query5, (int(x),))
            c1=[row[0] for row in mycursor.fetchall()]
            sql_query6="select quantity from retailer_cart where product_id='%s'"
            mycursor.execute(sql_query6, (int(x),))
            n3=[row[0] for row in mycursor.fetchall()]
        r1=n1[0]
        r2=n2[0]
        r3=n3[0]
        x=a[0]
        y=b[0]
        z=c[0]
        x1=a1[0]
        y1=b1[0]
        z1=c1[0]
        for i in range(1,r1):
          for j in range(1,r2):
            for k in range(1,r3):
                sumnum=x*i+y*j+z*k
                if(sumnum==100.0):
                    print('you can select {},{} {},{} {},{}'.format(i,x1,j,y1,k,z1))
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
          mycursor.execute(quer1,(int(storeid),int(sh_shopperid),disp_shoprname[0],(int(100))))     #insert row in cart_order
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
        else:
          print("invalid selection")
         

          
