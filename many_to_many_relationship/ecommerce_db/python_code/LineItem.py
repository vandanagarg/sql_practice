import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class LineItem:

    def __init__(self,order_id, prod_id):
        self.id = None
        self.order_id = order_id
        self.prod_id = prod_id
        self.quantity = fake_data.random_digit_not_null()
        self.price = fake_data.random_digit_not_null()
        
    def save(self):
        sql_form = "INSERT INTO \
                    line_item \
                        (order_id, prod_id, quantity,price)\
                    VALUES \
                        (%s,%s, %s, %s)"
        client.execute(sql_form, 
                      [
                      self.order_id, self.prod_id, self.quantity,self.price
                      ])        
        adapter.commit()

    @classmethod
    def any(cls,column_name, column_value):
        client.execute(f"Select * from line_item where {column_name} = {column_value}")
        result = client.fetchall()
        columns = client.column_names
        line_items_list = []
        for row in range(0, len(result)):
            line_item_object = {}
            for i in range(0, len(columns)):
                line_item_object[columns[i]] = result[row][i]
            line_items_list.append(line_item_object)            
        return line_items_list  

    @classmethod
    def find_by_order_id(cls,order_id):
        client.execute(f"Select * from line_item where order_id = {order_id} order by ID desc limit 1")
        result = client.fetchone()
        columns = client.column_names
        line_item_object = {}
        for i in range(0, len(columns)):
            line_item_object[columns[i]] = result[i]            
        return line_item_object 
      