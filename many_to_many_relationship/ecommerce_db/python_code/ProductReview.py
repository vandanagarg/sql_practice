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
      
      
      self.product_name = fake_data.random_elements(elements=("flour","sugar", "shirts",
                           "TV","mobile","books", "coat","jeans","dresses","hard disk"
                          "table", "chair","bottle","cosmetics"), length=1, unique=False)
      self.category = self.product_name
      self.quantity = fake_data.random_digit_not_null()
      self.encrypted_password = fake_data.lexify(text='?????????????', letters='*')
      self.title() = fake_data.lexify(text='???? ????? ???? ???',
                     letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      self.product_description = fake_data.lexify(text='???? ????? ???? ???', 
                                 letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      self.price = fake_data.random_digit_not_null()


        self.area = fake_data.city()
        self.specialist_in = fake_data.random_elements(elements=('skin', 'child', 'bones'), length=1, unique=False)
        self.working_hours = fake_data.random_elements(elements=('9AM to 12PM ', '12PM to 5PM', '11AM to 3PM'), length=1, unique=False)


    def save(self):
        sql_form = "INSERT INTO doctors(first_name, last_name, email, phone_number,area,specialist_in, working_hours ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        client.execute(sql_form, [self.first_name, self.last_name, self.email, self.phone_number, self.area , self.specialist_in[0], self.working_hours[0]])
        adapter.commit()

    @classmethod
    def random_doctor(cls):
        client.execute("Select * from doctors ORDER BY RAND() limit 1")
        result = client.fetchone()
        # print(result)
        columns = client.column_names
        doctor_object = {}
        for i in range(0, len(columns)):
            doctor_object[columns[i]] = result[i]            
        return doctor_object


