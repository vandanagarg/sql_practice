from SeqInsert import SeqInsert
from User import User
from Product import Product
from UserAddress import UserAddress
from ProductReview import ProductReview
from Images import Images
from Orders import UserOrders
from LineItem import LineItem
from CartProduct import CartProduct
import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class InsertData:

    def __init__(self):
        pass

    def insert_data(self):
        sq_insert = SeqInsert()

        for row in range(0,2):
            sq_insert.insert_user_data()
            current_user_id = sq_insert.read_user_id()
            print(current_user_id)

            sq_insert.insert_address(current_user_id)
            current_address_id = sq_insert.read_address_id(current_user_id)
            print(current_address_id)

            sq_insert.insert_order(current_user_id,current_address_id)
            current_order_id = sq_insert.read_order_id(current_user_id)

            sq_insert.insert_product_data()
            current_product_id = sq_insert.read_product_id()
            random_prod_id = sq_insert.random_product_id()


            for i in range(0,2):
                sq_insert.insert_images(current_product_id)
                sq_insert.insert_line_item(current_order_id, random_prod_id)
                line_item_product_id = sq_insert.read_line_item_product_id(current_order_id)
                sq_insert.insert_product_review(line_item_product_id,current_user_id )
                sq_insert.insert_cart_product(current_user_id, line_item_product_id)



insert_data = InsertData()
insert_data.insert_data()
