drop database one_to_many_db;
create database one_to_many_db;

use one_to_many_db;

CREATE TABLE user (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50),
phone_number VARCHAR(50),
date_of_birth DATE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
INDEX (firstname,lastname, email ));


CREATE TABLE user_address (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
user_id INT(6) UNSIGNED NOT NULL ,
house_no INT(6) NOT NULL,
street_address VARCHAR(30) NOT NULL,
city VARCHAR(20),
state_address VARCHAR(20) ,
pin INT(6) ,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
INDEX (user_id,state_address, pin ),
FOREIGN KEY (user_id) REFERENCES user(id)
);


desc user_address;

show indexes from user_address;


-- CREATE TABLE t1 (
--   col1 VARCHAR(10),
--   col2 VARCHAR(20),
--   INDEX (col1, col2(10))
-- );

-- CREATE INDEX autid ON newauthor(aut_id))