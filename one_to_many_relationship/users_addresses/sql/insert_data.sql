use one_to_many_db;

-- Table user insert

INSERT INTO user(firstname, lastname,email,phone_number ) VALUES ("vandana", "singla","vandana.singla", "+49");

select * from user;

--  Table user_address insert

INSERT INTO user_address (user_id, house_no, street_address,city,state_address,pin) VALUES (1,100, "ward 12", "Kurali","Punjab",140103);
INSERT INTO user_address (user_id, house_no, street_address,city,state_address,pin) VALUES (1,200, "ward 22", "Moga","Punjab", 104023);

select * from user_address;

