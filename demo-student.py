from datetime import datetime
from h11 import ConnectionClosed
import mysql.connector  

def insertStudent():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "schooldb"
    )
    myCursor = connection.cursor()
    sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
    ogrenciler = [
        ("101","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
        ("102","Ali","Can",datetime(2005,5,17),"E"),
        ("103","Canan","Tan",datetime(2005,5,17),"K"),
        ("104","Ayşe","Taner",datetime(2005,5,17),"K"),
        ("105","Bahadır","Toksöz",datetime(2005,5,17),"E"),
        ("106","Ali","Cenk",datetime(2005,5,17),"E")
    ]
    

    myCursor.executemany(sql,ogrenciler)
    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()


def getStudents():
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "schooldb"
    )
    myCursor = connection.cursor()

    sql = "Select COUNT(*) from student Where Gender='E'"
    myCursor.execute(sql)

    try:
        result = myCursor.fetchall()
        for student in result:
            print(f"Number: {student[0]} Name:")
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Kapandı")

def updateStudentsById(id):
    connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "schooldb"
    )
    myCursor = connection.cursor()

    sql = "Update student SET StudentNumber=%s, Name=%s,Surname=%s,Birthdate =%s, Gener=%s  from student Where id=%s"

    params = ()
    myCursor.execute(sql,params)
    try:
        connection.commit()
        print(f"{myCursor.rowcount} tane kayıt eklendi")
    except mysql.connector.Error as err:
        print("Hata",err)
    finally:
        connection.close()
        print("Kapandı")
    myCursor.execute(sql)

