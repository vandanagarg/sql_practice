#Python generate Fake data

from faker import Faker
fake = Faker()

name = fake.name()
print(name)

date = fake.date()
print(date)


# print("vandana")
