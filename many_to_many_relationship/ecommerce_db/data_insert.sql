USE practice_sql_db;

-- INSERT INTO `table_name`(column_1,column_2,...) VALUES (value_1,value_2,...);

-- Table user insert

INSERT INTO user(first_name, last_name,email) VALUES ("vandana", "garg" , "vg@gmail.com");
INSERT INTO user(first_name, last_name,email, user_status ) VALUES ("peeyush", "garg","peeyush.garg", 1 );
INSERT INTO user(first_name, last_name,email, user_status ) VALUES ("vandana", "singla","vandana.singla", 2 );
INSERT INTO user(first_name,last_name,email,encrypted_password,phone_number,user_status) VALUES ('peeyush', 'singla', 'peeyush@gmail.com', 'xyz', '+49' , 1 );


-- Table product insert

INSERT INTO product (product_name,category, quantity, title,product_description, price ) VALUES ("Atta","Flour", 2, "Wheat Flour","healthy weath fine grain", 200  );
INSERT INTO product (product_name,category, quantity, title,product_description, price ) VALUES ("chini","sugar", 2, "Wheat Flour","healthy weath fine grain", 200  );
INSERT INTO product (product_name,category, quantity, title,product_description, price ) VALUES ("namak","salt", 2, "iodine salt","salty", 100  );


-- Table user_address insert

INSERT INTO user_address (user_id, house_no, street_address,city) VALUES (1,100, "ward 12", "Kurali");
INSERT INTO user_address (user_id, house_no, street_address,city) VALUES (2,200, "ward 22", "Moga");

-- Table product_review insert

INSERT INTO product_review (prod_id, user_id ,stars, comments) VALUES (1,1, 3, "good" );
INSERT INTO product_review (prod_id, user_id ,stars, comments) VALUES (1,3, 1, "bad" );
INSERT INTO product_review (prod_id, user_id ,stars, comments) VALUES (2,1, 5, "nice" );
INSERT INTO product_review (prod_id, user_id ,stars, comments) VALUES (2,3, 3, "good" );

-- Table images insert

INSERT INTO images(prod_id, image_url, image_order) VALUES (1,"pic3",3);
INSERT INTO images(prod_id, image_url, image_order) VALUES (1,"pic4",4);
INSERT INTO images(prod_id, image_url, image_order) VALUES (1,"pic1",1);
INSERT INTO images(prod_id, image_url, image_order) VALUES (2,"pic2",2);
INSERT INTO images(prod_id, image_url, image_order) VALUES (2,"pic1",1);

-- Table orders insert

INSERT INTO orders(user_id, order_status,billing_address_id, shipping_address_id, payment_source) VALUES(1,"Booked", 1,2, "card");
INSERT INTO orders(user_id, order_status,billing_address_id, shipping_address_id, payment_source) VALUES(2,"Approved", 2,2, "cash");

-- Table line_item insert

INSERT INTO line_item (order_id, prod_id, quantity, price ) VALUES(1,1,2, 89.67);
INSERT INTO line_item (order_id, prod_id, quantity ) VALUES(1,2,2);
INSERT INTO line_item (order_id, prod_id, quantity, price ) VALUES(2,1,3, 289.67);
INSERT INTO line_item (order_id, prod_id, quantity, price ) VALUES(2,2,12, 2289.67);


-- Table cart_product insert

INSERT INTO cart_product (user_id, prod_id, quantity) VALUES(1,1,2);
INSERT INTO cart_product (user_id, prod_id, quantity) VALUES(1,2,3);
INSERT INTO cart_product (user_id, prod_id, quantity) VALUES(2,1,2);
INSERT INTO cart_product (user_id, prod_id, quantity) VALUES(2,2,3);

commit;
