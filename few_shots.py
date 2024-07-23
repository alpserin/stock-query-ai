few_shots = [
    {'Question' : "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "180"},
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': "116903.19"},
    {'Question': "If we have to sell all the nike tshirts today with discounts applied. How much revenue would we generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.discount_percentage,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, tshirt_id from tshirts where brand = 'nike'
group by tshirt_id) a left join discounts on a.tshirt_id = discounts.tshirt_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "111278.67355"} ,
     {'Question' : "If we have to sell all the skechers' T-shirts today. How much revenue our store will generate without discount?" ,
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'skechers'",
      'SQLResult': "Result of the SQL query",
      'Answer' : "174296.23"},
    {'Question': "How many white color adidas tshirts do I have?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'adidas' AND color = 'White'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "49"
     },
     {'Question': "how many tshirts do we have in total?",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM tshirts",
     'SQLResult': "Result of the SQL query",
     'Answer' : "10245"
     }
]