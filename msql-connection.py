import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", #192.23.48.56 Server olacak
    user = "root",
    password = "12345",
    database = "mydatabase"

)


myCursor = mydb.cursor()
myCursor.execute("CREATE TABLE  customers (name VARCHAR(255), address VARCHAR(255))")

# myCursor.execute("CREATE DATABASE mydatabase")
# print(mydb)

