# database_design

Database design is the organization of data according to a database model. 
The designer determines what data must be stored and how the data elements interrelate. 
With this information, they can begin to fit the data to the database model.
Database management system manages the data accordingly.

Database design involves classifying data and identifying interrelationships. 
This theoretical representation of the data is called an *`ontology`*. 
The ontology is the theory behind the database's design.

reference :sunglasses: : [Database design](https://en.wikipedia.org/wiki/Database_design)

Well, now the more confusing it sounds, the more important it is for a data engineer.

Next to python , the most important thing to learn is database.
It might just sound one thing to learn but no , it's journey that starts with SQL basics,
forming and debugging complex SQL queries, relationship models, database design, implementing
database design taking care of indexes, keys, constraints etc.... :sweat_smile:

So here in this repository [sql_practice](https://github.com/vandanagarg/sql_practice), 
I have implemented a few relationship models and maintained all the database design code.

### Project Description [sql_practice](https://github.com/vandanagarg/sql_practice)

**Language** :- Python, SQL

**Databases** :- MySQL

**Command Line** :- Terminal

**Tools/ IDE** :- Pycharm

**Version Control system** :- Git

**Operating System** :- MAC-OSX

**Text Editor** :- Visual Studio Code

**Python Packages/Modules** :- faker and mysql.connector


###### I have divided and structured the folders as per the different relationship models. Given below are the links and details of the different projects covered.

* [one_to_one_relationship](https://github.com/vandanagarg/sql_practice/tree/master/one_to_one_relationship)
   This project shows one to one relationship between user and their address. A single user can have only 1 address.
   
   I have also refactored the code using OOPS concepts: 
   [object_oriented_code](https://github.com/vandanagarg/sql_practice/blob/master/one_to_one_relationship/insert_data_object_oriented.py)

* [one_to_many_relationship](https://github.com/vandanagarg/sql_practice/tree/master/one_to_many_relationship)
   
    i. [users_addresses](https://github.com/vandanagarg/sql_practice/tree/master/one_to_many_relationship/users_addresses)
    This project shows one to many relationship between user and their address. A single user can have more than 1 address.
   Under this I have implemented the code both in 
   [python_code](https://github.com/vandanagarg/sql_practice/tree/master/one_to_many_relationship/users_addresses/python_code)
    and 
    [sql_code](https://github.com/vandanagarg/sql_practice/tree/master/one_to_many_relationship/users_addresses/sql).

* [many_to_many_relationship](https://github.com/vandanagarg/sql_practice/tree/master/many_to_many_relationship)

    i. [appointments_system](https://github.com/vandanagarg/sql_practice/tree/master/many_to_many_relationship/appointments_system)
        In this appointments_system project I have shown the relations between doctors, patients and the appointments.        
        
    ii. [ecommerce_db](https://github.com/vandanagarg/sql_practice/tree/master/many_to_many_relationship/ecommerce_db)
        I have implemented an ecommerce database and separated the code on the bases of python and sql code.
        The design shows the relations mainly between user, product and orders tables.
        

**P.S.** : I have implemented virtual projects and inserted fake data using *`faker`* module in Python.
           Also I haven't used any ORM to connect Python with MYSQL db, instead I have used *`mysql.connector`* module.

Looking for Data Engineering job opportunities in Berlin.
Got any reference, please reach out to me :smiley:
     
:email:  vandana.sde@gmail.com
   
:computer:  https://www.linkedin.com/in/vandana-garg/