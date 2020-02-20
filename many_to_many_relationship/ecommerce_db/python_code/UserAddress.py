import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class UserAddress:

    def __init__(self, user_id):
        self.id = None
        self.user_id = user_id
        self.house_no = fake_data.building_number()
        self.street_address = fake_data.street_name()
        self.city = fake_data.city()
        self.state_address = fake_data.state()
        self.pin = fake_data.zipcode()
        self.contact_person = fake_data.name()
        self.alternate_number = fake_data.phone_number()

    def save(self):
        sql_form = "INSERT INTO \
                    user_address \
                        (user_id, house_no, street_address, city,\
                        state_address, pin,contact_person,alternate_number)\
                    VALUES \
                        (%s,%s, %s, %s,%s,%s,%s,%s)"
        client.execute(sql_form, 
                      [
                      self.user_id, self.house_no, self.street_address, self.city, 
                      self.state_address, self.pin, self.contact_person, self.alternate_number
                      ])        
        adapter.commit()

    @classmethod
    def last(cls):
        client.execute("Select * from user_address order by id desc limit 1")
        result = client.fetchone()
        columns = client.column_names
        user_address_object = {}
        for i in range(0, len(columns)):
            user_address_object[columns[i]] = result[i]            
        return user_address_object     
      
    @classmethod
    def random(cls):
        client.execute("Select * from user_address ORDER BY RAND() limit 1")
        result = client.fetchone()
        # print(result)
        columns = client.column_names
        address_object = {}
        for i in range(0, len(columns)):
            address_object[columns[i]] = result[i]            
        return address_object
      
    @classmethod
    def find_by_user_id(cls,user_id):
        client.execute(f"Select * from user_address where user_id = {user_id}")
        result = client.fetchone()
        columns = client.column_names
        user_address_object = {}
        for i in range(0, len(columns)):
            user_address_object[columns[i]] = result[i]            
        return user_address_object 