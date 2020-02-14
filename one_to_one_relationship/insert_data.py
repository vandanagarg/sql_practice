import mysql.connector
from faker import Faker
fake_data = Faker()


adapter = mysql.connector.connect(user= "root", password="testing123", database= "one_to_one_db")
client = adapter.cursor()

def insert_user(row_data):
    sql_form = "INSERT INTO user(firstname, lastname,email,phone_number,date_of_birth ) VALUES (%s, %s, %s, %s, %s)"
    client.execute(sql_form, row_data)
    adapter.commit()

def user_data():
    data_row = [fake_data.first_name(), fake_data.last_name(), fake_data.email(), fake_data.phone_number(), fake_data.date(pattern='%Y-%m-%d', end_datetime=None)]
    return data_row

def insert_user_address_data(current_id):
    sql_form = "INSERT INTO user_address (user_id, house_no, street_address,city,state_address,pin) VALUES (%s,%s, %s, %s,%s,%s)"
    
    row_data = generate_row_data(current_id)
    client.execute(sql_form, row_data)
        
    adapter.commit()

def generate_row_data(current_user_id):

    create_dummy_data = [current_user_id, fake_data.building_number(), fake_data.street_name(), fake_data.city(), fake_data.state(), fake_data.zipcode()]
    # print(create_dummy_data)
    return create_dummy_data

def read_user_id():

    client.execute("Select id from user order by id desc limit 1")

    result = client.fetchall()
    # print(result)
    # print((client.column_names[0]))
    list_of_id = []
    # i = int((len(result)) -1)
    list_of_id.append(result[0][0])
    return list_of_id

def insert_data(row_count):
    for i in range(0, row_count):
        row_data = user_data()
        # print(row_data)
        insert_user(row_data)
        adapter.commit()
        user_id = read_user_id()
        # print(user_id[0])
        insert_user_address_data(user_id[0])


insert_data(5)