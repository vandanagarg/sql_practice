import mysql.connector


adapter = mysql.connector.connect(user= "root", password= "testing123", database = "one_to_many_db")
client = adapter.cursor()

def read_user_id():

    client.execute("Select id from user")

    result = client.fetchall()
    # print(result)
    list_of_id = []
    for i in range(0, len(result)):
        list_of_id.append(result[i][0])
    return list_of_id

    # print((client.column_names[0]))



# print(read_user_id())




 
