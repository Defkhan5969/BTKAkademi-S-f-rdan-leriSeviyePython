import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()

    # myCursor.execute("Select * From Products ")
    myCursor.execute("Select * From Products Order By name, price ASC")

    try:
        result = myCursor.fetchall()
        for product in result: 
            # print(f"name {product[1]} Fiyat: {product[2]} \n")
            print(f"id {product[0]} name: {product[1]} price: {product[2]}")
    # result = myCursor.fetchone()
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Kapatıldı")

  


def getProductsById(id):
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()
    sql = "Select * From Products Where id=%s"
    params = (id,)
    # myCursor.execute("Select * From Products ")
    myCursor.execute(sql,params)

    result = myCursor.fetchall()
    # result = myCursor.fetchone()

    for product in result: 
        # print(f"name {product[1]} Fiyat: {product[2]} \n")
        print(f"id {product[0]} name: {product[2]}")

getProducts()