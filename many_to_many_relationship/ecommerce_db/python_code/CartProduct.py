import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class CartProduct:

    def __init__(self,user_id, prod_id):
        self.id = None
        self.user_id = user_id
        self.prod_id = prod_id
        self.quantity = fake_data.random_digit_not_null()
        
    def save(self):
        sql_form = "INSERT INTO \
                    cart_product \
                        (user_id, prod_id, quantity)\
                    VALUES \
                        (%s,%s, %s)"
        client.execute(sql_form, 
                      [
                      self.user_id, self.prod_id, self.quantity
                      ])        
        adapter.commit()

    @classmethod
    def any(cls,column_name, column_value):
        client.execute(f"Select * from cart_product where {column_name} = {column_value}")
        result = client.fetchall()
        columns = client.column_names
        cart_list = []
        for row in range(0, len(result)):
            cart_object = {}
            for i in range(0, len(columns)):
                cart_object[columns[i]] = result[row][i]
            cart_list.append(cart_object)            
        return cart_list  