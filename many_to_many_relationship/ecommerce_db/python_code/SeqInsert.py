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

class SeqInsert:

    def __init__(self):
        pass

    def insert_user_data(self):
        user = User()
        user.save()

    def read_user_id(self):
        current_user = User.last()
        return current_user["id"]

    def insert_address(self, current_user_id):
        address = UserAddress(current_user_id)
        address.save()

    def read_address_id(self, current_user_id):
        current_address_id = UserAddress.find_by_user_id(current_user_id)
        return current_address_id["id"]

    def insert_order(self,current_user_id,current_address_id):
        order = UserOrders(current_user_id,current_address_id)
        order.save()

    def read_order_id(self, current_user_id):
        current_order = UserOrders.find_by_user_id(current_user_id)
        return current_order["id"]

    def insert_product_data(self):
        product = Product()
        product.save()

    def read_product_id(self):
        current_product = Product.last()
        return current_product["id"]

    def random_product_id(self):
        random_product = Product.random()
        return random_product["id"]

    def insert_images(self, current_product_id):
        image = Images(current_product_id)
        image.save()

    def insert_line_item(self, current_order_id, random_prod_id):
        line_item = LineItem(current_order_id, random_prod_id)
        line_item.save()

    def read_line_item_product_id(self,current_order_id):
        line_item_product = LineItem.find_by_order_id(current_order_id)
        return line_item_product["prod_id"]

    def insert_product_review(self,current_user_id, line_item_product_id):
        product_review = ProductReview(current_user_id, line_item_product_id)
        product_review.save()

    def insert_cart_product(self,current_user_id, line_item_product_id):
        cart_product = CartProduct(current_user_id, line_item_product_id)
        cart_product.save()
