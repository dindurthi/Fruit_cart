import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  db="fruits"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(111,11,'Banana',20,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(112,11,'Orange',10,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(113,11,'Apple',15,5)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(114,11,'Watermelon',25,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(115,11,'Papaya',20,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(116,11,'Mango',50,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(117,11,'PineApple',15,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(118,11,'Pomegranate',20,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(119,11,'Guava',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(121,12,'Banana',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(122,12,'Orange',10,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(123,12,'Apple',15,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(124,12,'Watermelon',25,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(125,12,'Papaya',20,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(126,12,'Mango',50,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(127,12,'PineApple',15,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(128,12,'Pomegranate',20,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(129,12,'Guava',20,4)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(131,13,'Banana',20,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(132,13,'Orange',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(133,13,'Apple',25,5)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(134,13,'Watermelon',25,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(135,13,'Papaya',20,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(136,13,'Mango',20,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(137,13,'PineApple',25,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(138,13,'Pomegranate',20,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(139,13,'Guava',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(141,14,'Banana',50,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(142,14,'Orange',20,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(143,14,'Apple',50,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(144,14,'Watermelon',50,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(145,14,'Papaya',50,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(146,14,'Mango',50,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(147,14,'PineApple',50,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(148,14,'Pomegranate',50,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(149,14,'Guava',50,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(151,15,'Banana',100,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(152,15,'Orange',100,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(153,15,'Apple',100,5)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(154,15,'Watermelon',100,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(155,15,'Papaya',100,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(156,15,'Mango',100,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(157,15,'PineApple',100,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(158,15,'Pomegranate',100,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(159,15,'Guava',100,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(161,16,'Banana',20,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(162,16,'Orange',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(163,16,'Apple',25,5)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(164,16,'Watermelon',25,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(165,16,'Papaya',20,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(166,16,'Mango',20,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(167,16,'PineApple',25,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(168,16,'Pomegranate',20,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(169,16,'Guava',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(171,17,'Banana',50,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(172,17,'Orange',20,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(173,17,'Apple',50,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(174,17,'Watermelon',50,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(175,17,'Papaya',50,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(176,17,'Mango',50,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(177,17,'PineApple',50,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(178,17,'Pomegranate',50,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(179,17,'Guava',50,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(181,18,'Banana',20,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(182,18,'Orange',10,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(183,18,'Apple',15,5)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(184,18,'Watermelon',25,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(185,18,'Papaya',20,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(186,18,'Mango',50,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(187,18,'PineApple',15,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(188,18,'Pomegranate',20,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(189,18,'Guava',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(191,19,'Banana',20,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(192,19,'Orange',10,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(193,19,'Apple',15,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(194,19,'Watermelon',25,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(195,19,'Papaya',20,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(196,19,'Mango',50,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(197,19,'PineApple',15,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(198,19,'Pomegranate',20,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(199,19,'Guava',20,4)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1101,110,'Banana',100,1)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1102,110,'Orange',100,2)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1103,110,'Apple',100,5)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1104,110,'Watermelon',100,10)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1105,110,'Papaya',100,8)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1106,110,'Mango',100,15)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1107,110,'PineApple',100,20)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1108,110,'Pomegranate',100,12)")
mycursor.execute("INSERT INTO retailer_cart (product_id,store_id,item,quantity,price) VALUES(1109,110,'Guava',100,2)")
mydb.commit()
print("Data inserted")



  
    
                  

     
