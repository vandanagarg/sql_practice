import mysql.connector
from faker import Faker
fake_data = Faker()


adapter = mysql.connector.connect(user= "root", password="testing123", database= "one_to_one_db")
client = adapter.cursor()

class User:
    def __init__(self):
        self.id = None
        self.firstname = fake_data.first_name()
        self.lastname = fake_data.last_name()
        self.email = fake_data.email()
        self.phone_number = fake_data.phone_number()
        self.date_of_birth = fake_data.date(pattern='%Y-%m-%d', end_datetime=None)

        
    def save(self):        
        sql_form = "INSERT INTO user(firstname, lastname, email, phone_number, date_of_birth ) VALUES (%s, %s, %s, %s, %s)"
        client.execute(
            sql_form, 
            [ self.firstname, self.lastname, self.email, self.phone_number, self.date_of_birth]
        )
        adapter.commit()
    

    @classmethod
    def last(cls):
        client.execute("Select * from user order by id desc limit 1")
        result = client.fetchone()
        columns = client.column_names
        user_object = {}
        for i in range(0, len(columns)):
            user_object[columns[i]] = result[i]            
        return user_object        


class Address:
    def __init__(self, user_id):
        self.id = None
        self.user_id = user_id
        self.house_no = fake_data.building_number()
        self.street_address = fake_data.street_name()
        self.city = fake_data.city()
        self.state_address = fake_data.state()
        self.pin = fake_data.zipcode()

    def save(self):
        sql_form = "INSERT INTO user_address (user_id, house_no, street_address, city, state_address, pin) VALUES (%s,%s, %s, %s,%s,%s)"
        client.execute(sql_form, [
            self.user_id, self.house_no, self.street_address, self.city, self.state_address, self.pin
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



# first_user = User()    
# first_user.save()
# user = User.last()

# first_address = Address(user['id'])
# first_address.save()
# address = Address.last()
# print(user)
# print(address)


def insert_rows(row_count):
    for i in range(0, row_count):
        first_user = User()    
        first_user.save()
        user = User.last()

        first_address = Address(user['id'])
        first_address.save()
        address = Address.last()
        print(user)
        print(address)
        


insert_rows(5)
