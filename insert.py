from ast import While
import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,image_url,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    myCursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{myCursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın Id {myCursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Bağlantı kapandı")

def insertProducts(list):
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,image_url,description) VALUES (%s,%s,%s,%s)"
    values = list

    myCursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{myCursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın Id {myCursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Bağlantı kapandı")
list = []
while True:
    name = input("Ürün adı: ")
    price = int(input("Ürün Fiyatı: "))
    imageUrl = input("Ürün resmi : ")
    description = input("Ürün açıklaması : ")

    list.append((name,price,imageUrl,description))

    result = input("Devam Etmek istiyor musunuz? (e/h)")
    if result =="h":
        print("Kayıtlarınız veri tabanınına aktarılıyor")
        print(list)
        insertProducts(list)
        break
    else:
        pass

insertProduct(name,price,imageUrl,description)