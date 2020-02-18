import User
import Product
import UserAddress
import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()


user = User.User()    
user.save()
user1 = User.User.random_user()
# print(user1)

product = Product.Product()    
product.save()
product1 = Product.Product.random_product()
# print(product1)

address = UserAddress.UserAddress(user1['id'])
address.save()
user_address = UserAddress.UserAddress.last_address()
# print(user_address)

