import mysql.connector
from selecting import getProducts

def deleteProduct(id):
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()
    
    sql = "delete from products where name LIKE %s"
    
    params = (id,)

    myCursor.execute(sql,params)


    try:
        connection.commit()
        print(f"{myCursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print("Hata",err)

    finally:
        connection.close()
        print("Kapandı")
deleteProduct("%S8%")
getProducts()