import mysql.connector
from read_data import read_user_id
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password="testing123", database= "one_to_many_db")
client = adapter.cursor()

user_ids = read_user_id()

def insert_data():

    for i in range(0, len(user_ids)):
        sql_form = "INSERT INTO user_address (user_id, house_no, street_address,city,state_address,pin) VALUES (%s,%s, %s, %s,%s,%s)"
        
        current_id = user_ids[i]
        row_data = generate_row_data(current_id)
        client.execute(sql_form, row_data)

        row_data = generate_row_data(current_id)
        client.execute(sql_form, row_data)
        
        adapter.commit()

def generate_row_data(current_user_id):

    create_dummy_data = [current_user_id, fake_data.building_number(), fake_data.street_name(), fake_data.city(), fake_data.state(), fake_data.zipcode()]
    # print(create_dummy_data)
    return create_dummy_data

insert_data()
