drop database practice_sql_db;
create database practice_sql_db;

use practice_sql_db;

CREATE TABLE user (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(130) NOT NULL,
    last_name VARCHAR(130) NOT NULL,
    email VARCHAR(150) NOT NULL,
    encrypted_password VARCHAR(225),
    phone_number VARCHAR(50),
    date_of_birth DATE,
    user_status INT(3),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (email),
    INDEX name(first_name,last_name ) comment 'By first name and/or last name'
);

CREATE TABLE product (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(130) NOT NULL,
    category VARCHAR(130) NOT NULL,
    quantity INT(3),
    title VARCHAR(225),
    product_description VARCHAR(225),
    price INT(6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (product_name, category)
);

CREATE TABLE user_address (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT(6) UNSIGNED NOT NULL,
    house_no INT(6) NOT NULL,
    street_address VARCHAR(130) NOT NULL,
    city VARCHAR(220),
    state_address VARCHAR(220),
    pin INT(6),
    contact_person VARCHAR(220),
    alternate_number VARCHAR(225),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (user_id),
    INDEX place(city, state_address),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE product_review (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    prod_id INT(6) UNSIGNED NOT NULL,
    user_id INT(6) UNSIGNED NOT NULL,
    stars INT(6),
    comments VARCHAR(225),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (prod_id) REFERENCES product(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE images (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    prod_id INT(6) UNSIGNED NOT NULL,
    image_url VARCHAR(225) NOT NULL,
    image_order INT(6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (prod_id, image_order),
    FOREIGN KEY (prod_id) REFERENCES product(id)
);

CREATE TABLE orders (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT(6) UNSIGNED NOT NULL,
    order_status VARCHAR(30) NOT NULL,
    billing_address_id INT(6) UNSIGNED NOT NULL,
    shipping_address_id INT(6) UNSIGNED NOT NULL,
    payment_source VARCHAR(20),
    excpected_delivery_date DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (user_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (billing_address_id) REFERENCES user_address(id),
    FOREIGN KEY (shipping_address_id) REFERENCES user_address(id) 
);

CREATE TABLE line_item (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id INT(6) UNSIGNED NOT NULL,
    prod_id INT(6) UNSIGNED NOT NULL,
    quantity INT(6) NOT NULL,
    price float,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE INDEX (order_id,prod_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (prod_id) REFERENCES product(id)
);

CREATE TABLE cart_product (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id INT(6) UNSIGNED NOT NULL,
    prod_id INT(6) UNSIGNED NOT NULL,
    quantity INT(6) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (user_id,prod_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (prod_id) REFERENCES product(id)
);



