import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="py_db"
)

# print(mydb) # shows connections of object

mycursor = mydb.cursor()

''' shows the list of schema '''
# print("List of Schema..")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)


''' create database or schema '''
# mycursor.execute("CREATE DATABASE py_db")
'''op: Process finished with exit code 0'''

''' Delete Schema '''
# sql = "DROP SCHEMA py_db2" '''OR'''
# sql = "DROP DATABASE py_db2"
# sql = "DROP TABLE customers" '''OR'''
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)


''' create table '''
# mycursor.execute("CREATE TABLE req_res (id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), req TEXT, res TEXT)")


''' create record '''
# sql = "INSERT INTO req_res (name, req, res) VALUES (%s, %s, %s)"
# val = ("John", "Highway 21", "kuch bhe")
# mycursor.execute(sql, val) #op: 1 record inserted.
#(multiple value insert)
# val = [
#   ('Peter', 'Lowstreet', '4'),
#   ('Amy', 'Apple st', '652'),
#   ('Hannah', 'Mountain', '21'),
#   ('Chuck', 'Main Road', '989'),
#   ('Viola', 'Sideway', '1633')
# ]
# mycursor.executemany(sql, val) #op: 5 record inserted.
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
#(Get Inserted ID)
# print("1 record inserted, ID:", mycursor.lastrowid) #op: 1 record inserted, ID: 8


''' update record '''
# sql = "UPDATE req_res SET name = 'Dev' WHERE id = 3"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected or updated")


''' read record '''
# mycursor.execute("SELECT * FROM req_res")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


''' delete record '''
# sql = "DELETE FROM req_res WHERE name = 'chuck'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

''' where statment '''
# sql = "SELECT * FROM req_res WHERE name='Dev'"
# mycursor.execute(sql)
# result = mycursor.fetchall()
# for x in result:
#     print(x)

''' wildcard characters '''
# sql = "SELECT * FROM req_res WHERE name LIKE '%de%'"
# mycursor.execute(sql)
# result = mycursor.fetchall()
# for x in result:
#     print(x)

''' prvent sql injection '''
# sql = "SELECT * FROM req_res WHERE name = %h"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

''' join '''
# sql = "SELECT \
#   rr.name AS rr_name, \
#   rr.res AS rr_req \
#   FROM req_res as rr \
#   INNER JOIN products ON rr.name = products.name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

''' limit '''
# sql = "SELECT * FROM req_res LIMIT 5"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

''' limit with offset '''
# sql = "SELECT * FROM req_res LIMIT 5 OFFSET 3"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)