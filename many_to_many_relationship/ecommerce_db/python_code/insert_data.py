import User
import Product
import UserAddress
import ProductReview
from Images import Images
from Orders import UserOrders
from LineItem import LineItem
from CartProduct import CartProduct
import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()


# user = User.User()    
# user.save()
user1 = User.User.random()
# print(user1)

# product = Product.Product()    
# product.save()
product1 = Product.Product.random()
# print(product1)

# for i in range(0,100):
#     address = UserAddress.UserAddress(user1['id'])
#     address.save()
# user_address = UserAddress.UserAddress.last()
# print(user_address)

# print(user1['id'])
# user_address = UserAddress.UserAddress.find_by_user_id(user1['id'])
# print(user_address)

# for i in range(0, 2000):
#     user1 = User.User.random()
#     product1 = Product.Product.random()
#     product_review = ProductReview.ProductReview(product1['id'],user1['id'])
#     product_review.save()

# print(user1['id'])
# review1 = ProductReview.ProductReview.any("user_id",3)
# review1 = ProductReview.ProductReview.any("user_id", user1['id'])
# print(review1)

# print(product1['id'])
# review2 = ProductReview.ProductReview.any("prod_id",2)
# review2 = ProductReview.ProductReview.any("prod_id",product1['id'])
# print(review2)

# for i in range(0,5000):
#     product1 = Product.Product.random()
#     product_image = Images(product1['id'])
#     product_image.save()

# image1 = Images.all()
# print(image1)

# image2 = Images.any("prod_id", 2)
# print(image2)
# image3 = Images.any("image_order", 4)
# print(image3)


# for i in range(0,5000):
#     user1 = User.User.random()
#     billing_address = UserAddress.UserAddress.random()
#     shipping_address = UserAddress.UserAddress.random()
#     order = UserOrders(user1['id'], billing_address['id'], shipping_address['id'])
#     order.save()

# order1 = UserOrders.random()
# print(order1)

# order2 = UserOrders.any("shipping_address_id", 2)
# print(order2)


# for i in range(0,2):
#     order1 = UserOrders.random()
#     product1 = Product.Product.random()
#     line_item = LineItem(order1['id'],product1['id'])
#     line_item.save()

# line_item1 = LineItem.any("order_id",2)
# print(line_item1)


for i in range(0,2):
    user1 = User.User.random()
    product1 = Product.Product.random()
    cart_product = CartProduct(user1['id'],product1['id'])
    cart_product.save()

cart_product1 = CartProduct.any("user_id", 2)
print(cart_product1)