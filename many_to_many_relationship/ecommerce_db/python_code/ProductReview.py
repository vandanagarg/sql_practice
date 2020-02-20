import mysql.connector
from faker import Faker
fake_data = Faker()

adapter = mysql.connector.connect(user= "root", password= "testing123", database="practice_sql_db")
client = adapter.cursor()

class ProductReview:

    def __init__(self, prod_id, user_id):
        self.id = None
        self.prod_id = prod_id
        self.user_id = user_id
        self.stars = fake_data.random_elements(elements=(1,2,3,4,5), length=1, unique=False)
        self.comments = fake_data.lexify(text='???? ????? ???? ???',
                        letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
    def save(self):
        sql_form = "INSERT INTO \
                    product_review \
                        (prod_id, user_id, stars, comments)\
                    VALUES \
                        (%s,%s, %s, %s)"
        client.execute(sql_form, 
                      [
                      self.prod_id, self.user_id, self.stars[0], self.comments
                      ])        
        adapter.commit()

    @classmethod
    def all(cls):
        client.execute("Select * from product_review")
        result = client.fetchall()
        columns = client.column_names
        product_reviews_list = []
        for row in range(0, len(result)):
            review_object = {}
            for i in range(0, len(columns)):
                review_object[columns[i]] = result[row][i]            
            product_reviews_list.append(review_object)
        return product_reviews_list

    @classmethod
    def any(cls,column_name, column_value):
        client.execute(f"Select * from product_review where {column_name} = {column_value}")
        result = client.fetchone()
        columns = client.column_names
        review_object = {}
        for i in range(0, len(columns)):
            review_object[columns[i]] = result[i]            
        return review_object 