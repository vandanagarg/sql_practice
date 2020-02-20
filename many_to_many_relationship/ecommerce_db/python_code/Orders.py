import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class UserOrders:

    def __init__(self, user_id,billing_address_id):
        self.id = None
        self.user_id = user_id
        self.order_status = fake_data.random_elements(elements=('Booked', 'Confirmed', 'Cancelled','Delivered'), length=1, unique=False)
        self.billing_address_id = billing_address_id
        self.shipping_address_id = billing_address_id
        self.payment_source = fake_data.random_elements(elements=('Cash', 'Card', 'Credit','EMI'), length=1, unique=False)
        self.excpected_delivery_date = fake_data.date(pattern='%Y-%m-%d', end_datetime=None)
        
    def save(self):
        sql_form = "INSERT INTO \
                    orders \
                        (user_id, order_status, billing_address_id,\
                        shipping_address_id, payment_source, excpected_delivery_date)\
                    VALUES \
                        (%s,%s, %s, %s,%s, %s)"
        client.execute(sql_form, 
                      [
                      self.user_id, self.order_status[0], self.billing_address_id,
                      self.shipping_address_id, self.payment_source[0], 
                      self.excpected_delivery_date
                      ])        
        adapter.commit()
    
    @classmethod
    def random(cls):
        client.execute("Select * from orders ORDER BY RAND() limit 1")
        result = client.fetchone()
        # print(result)
        columns = client.column_names
        orders_object = {}
        for i in range(0, len(columns)):
            orders_object[columns[i]] = result[i]            
        return orders_object
    
    @classmethod
    def any(cls,column_name, column_value):
        client.execute(f"Select * from orders where {column_name} = {column_value}")
        result = client.fetchall()
        columns = client.column_names
        orders_list = []
        for row in range(0, len(result)):
            orders_object = {}
            for i in range(0, len(columns)):
                orders_object[columns[i]] = result[row][i]
            orders_list.append(orders_object)            
        return orders_list     
      
    @classmethod
    def find_by_user_id(cls,user_id):
        client.execute(f"Select * from orders where user_id = {user_id}")
        result = client.fetchone()
        columns = client.column_names
        user_order_object = {}
        for i in range(0, len(columns)):
            user_order_object[columns[i]] = result[i]            
        return user_order_object 
      