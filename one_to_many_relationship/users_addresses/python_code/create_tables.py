import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password="testing123", database= "one_to_many_db")
client = adapter.cursor()


client.execute (\
"CREATE TABLE users (\
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
firstname VARCHAR(30) NOT NULL,\
lastname VARCHAR(30) NOT NULL,\
email VARCHAR(50),\
phone_number VARCHAR(50),\
date_of_birth DATE,\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
INDEX (firstname,lastname, email ))" )

client.execute (\
" CREATE TABLE user_addresses ( \
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
user_id INT(6) UNSIGNED NOT NULL ,\
house_no INT(6) NOT NULL,\
street_address VARCHAR(30) NOT NULL,\
city VARCHAR(20),\
state_address VARCHAR(20) ,\
pin INT(6) ,\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
INDEX (user_id,state_address, pin ),\
FOREIGN KEY (user_id) REFERENCES user(id)\
)" )
