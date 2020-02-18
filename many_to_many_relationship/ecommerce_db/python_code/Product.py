import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class Product:

    def __init__(self):
      self.id = None
      self.product_name = fake_data.random_elements(elements=("flour","sugar", "shirts",
                           "TV","mobile","books", "coat","jeans","dresses","hard disk"
                          "table", "chair","bottle","cosmetics"), length=1, unique=False)
      self.category = self.product_name
      self.quantity = fake_data.random_digit_not_null()
      self.title = fake_data.lexify(text='???? ????? ???? ???',
                     letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      self.product_description = fake_data.lexify(text='???? ????? ???? ???', 
                                 letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
      self.price = fake_data.random_digit_not_null()

    def save(self):
        sql_form = "INSERT INTO \
                    product \
                        (\
                        product_name, category, quantity, title,product_description, price \
                        )\
                    VALUES \
                        (%s, %s, %s, %s, %s, %s)"
        client.execute(sql_form, 
                      [
                        self.product_name[0], self.category[0], self.quantity, 
                        self.title, self.product_description , self.price
                      ])
        adapter.commit()

    @classmethod
    def random_product(cls):
        client.execute("Select * from product ORDER BY RAND() limit 1")
        result = client.fetchone()
        # print(result)
        columns = client.column_names
        product_object = {}
        for i in range(0, len(columns)):
            product_object[columns[i]] = result[i]            
        return product_object



# for i in range(0, 2000):
#     product = Product()    
#     product.save()


# product1 = Product.random_product()
# print(product1)



