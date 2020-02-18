import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password="testing123", database= "one_to_many_db")
client = adapter.cursor()

def insert_user(row_data):
    sql_form = "INSERT INTO user(firstname, lastname,email,phone_number ) VALUES (%s, %s, %s, %s)"
    client.executemany(sql_form, row_data)
    adapter.commit()

def user_data(row_count):
    data_row = []
    for i in range(0, row_count):
        single_row = [fake_data.first_name(), fake_data.last_name(), fake_data.email(), fake_data.phone_number()]
        data_row.append(single_row)
    return data_row

def insert_data(row_count):
    row_data = user_data(row_count)
    # print(row_data)
    insert_user(row_data)

insert_data(20)