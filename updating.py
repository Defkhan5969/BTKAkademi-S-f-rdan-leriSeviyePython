import errno
from turtle import update
import mysql.connector

from selecting import getProducts

def updateProduct(id,name,price):
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()
    if not name:
        sql = "Update products Set name = %s,price=%s where id=%s"
    
    params = (name,price,id)

    myCursor.execute(sql,params)


    try:
        connection.commit()
        print(f"{myCursor.rowcount} tane kayıt eklendi")
    except mysql.connector.Error as err:
        print("Hata",err)

    finally:
        connection.close()
        print("Kapandı")

    
updateProduct(1,"Iphone 8",6000)
getProducts()