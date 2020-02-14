import mysql.connector


adapter = mysql.connector.connect(user= "root", password="testing123", database= "one_to_one_db")
client = adapter.cursor()


client.execute (
"CREATE TABLE user (\
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
firstname VARCHAR(30) NOT NULL,\
lastname VARCHAR(30) NOT NULL,\
email VARCHAR(50) NOT NULL,\
phone_number VARCHAR(50),\
date_of_birth DATE,\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
UNIQUE INDEX (email),\
INDEX name(firstname,lastname ) comment 'By first name and/or last name' )" )

client.execute (
" CREATE TABLE user_address ( \
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
user_id INT(6) UNSIGNED NOT NULL ,\
house_no INT(6) NOT NULL,\
street_address VARCHAR(30) NOT NULL,\
city VARCHAR(20),\
state_address VARCHAR(20) NOT NULL,\
pin INT(6) NOT NULL,\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
UNIQUE INDEX (user_id),\
INDEX state(state_address, pin ),\
FOREIGN KEY (user_id) REFERENCES user(id)\
)" )

