

import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()

    # sql="Select * from products"
    # sql="Select * from Categories"
    # sql="Select * from products inner join Categories on Categories.id=Products.category_id"
    # sql="Select products.name,products.price,Categories.name from products inner join Categories on Categories.id=Products.category_id"
    # sql="Select * from products inner join Categories on Categories.id=Products.category_id where Categories.name='telefon'"
    sql="Select * from products as P inner join Categories as C on C.id=P.category_id where P.name='SamsungS10'"
    myCursor.execute(sql)

    try:
        result = myCursor.fetchall()
        for product in result: 
            print(product)
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Kapatıldı")

getProducts()