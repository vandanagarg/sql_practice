import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class Images:

    def __init__(self, prod_id):
        self.id = None
        self.prod_id = prod_id
        self.image_url = fake_data.image_url(width=None, height=None)
        self.image_order = fake_data.random_elements(elements=(1,2,3,4), length=1, unique=False)
        
    def save(self):
        sql_form = "INSERT INTO \
                    images \
                        (prod_id, image_url, image_order)\
                    VALUES \
                        (%s,%s, %s)"
        client.execute(sql_form, 
                      [
                      self.prod_id, self.image_url, self.image_order[0]
                      ])        
        adapter.commit()

    @classmethod
    def all(cls):
        client.execute("Select * from images")
        result = client.fetchall()
        columns = client.column_names
        images_list = []
        for row in range(0, len(result)):
            image_object = {}
            for i in range(0, len(columns)):
                image_object[columns[i]] = result[row][i]            
            images_list.append(image_object)
        return images_list

    @classmethod
    def any(cls,column_name, column_value):
        client.execute(f"Select * from images where {column_name} = {column_value}")
        result = client.fetchall()
        columns = client.column_names
        images_list = []
        for row in range(0, len(result)):
            image_object = {}
            for i in range(0, len(columns)):
                image_object[columns[i]] = result[row][i]
            images_list.append(image_object)            
        return images_list 