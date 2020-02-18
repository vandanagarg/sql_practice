import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class User:

    def __init__(self):
      self.id = None
      self.first_name = fake_data.first_name()
      self.last_name = fake_data.last_name()
      self.email = fake_data.email()
      self.encrypted_password = fake_data.lexify(text='?????????????', letters='*')
      self.phone_number = fake_data.phone_number()
      self.date_of_birth = fake_data.date(pattern='%Y-%m-%d', end_datetime=None)
      self.user_status = fake_data.random_elements(elements=(0, 1, 2), length=1, unique=False)

    def save(self):
        sql_form = "INSERT INTO \
                    user\
                        (first_name, last_name, email,encrypted_password, phone_number,\
                        date_of_birth,user_status)\
                    VALUES\
                        (%s, %s, %s, %s, %s, %s, %s)"
        
        client.execute(sql_form,
                        [
                        self.first_name, self.last_name, self.email, self.encrypted_password,
                        self.phone_number, self.date_of_birth, self.user_status[0]
                        ]
                      )
        adapter.commit()

    @classmethod
    def random_user(cls):
        client.execute("Select * from user ORDER BY RAND() limit 1")
        result = client.fetchone()
        # print(result)
        columns = client.column_names
        user_object = {}
        for i in range(0, len(columns)):
            user_object[columns[i]] = result[i]            
        return user_object


# for i in range(0, 2):
#     user = User()    
#     user.save()


# user1 = User.random_user()
# print(user1)


