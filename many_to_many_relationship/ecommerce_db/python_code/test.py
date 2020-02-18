from faker import Faker
fake_data = Faker()
 
cat = (fake_data.random_elements(elements=("flour","sugar", "shirts",
                           "TV","mobile","books", "coat","jeans","dresses","hard disk"
                          "table", "chair","bottle","cosmetics"), length=1, unique=False))

print(type(cat[0]))

print(cat[0])