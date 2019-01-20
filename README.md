# Fruit_cart

Fruit cart contains a set of retailers who sell the fruits mentioned below at different prices. They hold different quantities of the mentioned fruits.

1. Banana
2. Orange
3. Apple
4. Watermelon
5. Papaya
6. Mango
7. PineApple
8. Pomegranate
9. Guava

MySQL database named fruits is created. The tables in the database include [Tables](/tables_in_database.py)
<p>Retailer_cart displays fruits from all retailers and allows shopper to select a store to shop from. Shopper chooses from all combinations of selecting three fruits from the list. </p>

Based on the chosen combination, the given condition is verified by checking the condition _ax+by+cz=d_ where a,b,c are the prices of the items and x,y,z are valid quantities that satisfy the condition.

After obtaining valid quantities of x,y and z ,new rows are inserted into order_details and cart_order tables and the quantities are updated in the retailer_cart table.

  
  
  
