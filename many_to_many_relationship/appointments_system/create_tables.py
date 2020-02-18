import mysql.connector

adapter = mysql.connector.connect(user= "root", password= "testing123", database= "many_to_many_db")
client = adapter.cursor()


client.execute(
" CREATE TABLE doctors (\
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
first_name VARCHAR(30) NOT NULL,\
last_name VARCHAR(30) NOT NULL,\
email VARCHAR(50) NOT NULL,\
phone_number VARCHAR(50),\
area VARCHAR(50),\
specialist_in   VARCHAR(50) ,\
working_hours VARCHAR(50),\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
UNIQUE INDEX (email),\
INDEX speciality(specialist_in), \
INDEX name(first_name,last_name ) comment 'By first name and/or last name' )" )

client.execute(
" CREATE TABLE patients ( \
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
first_name VARCHAR(30) NOT NULL,\
last_name VARCHAR(30) NOT NULL,\
age INT(6) ,\
sex VARCHAR(3) NOT NULL,\
city VARCHAR(20),\
state_address VARCHAR(20) NOT NULL,\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
INDEX state(city, state_address ),\
INDEX name(first_name,last_name ) comment 'By first name and/or last name'    \
)" )


client.execute(
" CREATE TABLE appointments ( \
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
doctor_id INT(6) UNSIGNED NOT NULL ,\
patient_id INT(6) UNSIGNED NOT NULL ,\
concerned_problem VARCHAR(225) NOT NULL,\
appointment_time DATE NOT NULL,\
appointment_day VARCHAR(20) NOT NULL,\
booking_status VARCHAR(20) ,\
approval VARCHAR(20) ,\
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,\
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
INDEX ids(doctor_id,patient_id),\
INDEX day(appointment_day),\
FOREIGN KEY (doctor_id) REFERENCES doctors(id),\
FOREIGN KEY (patient_id) REFERENCES patients(id)\
)" )
