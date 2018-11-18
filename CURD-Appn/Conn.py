import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)

# print(mydb) # shows connections of object

