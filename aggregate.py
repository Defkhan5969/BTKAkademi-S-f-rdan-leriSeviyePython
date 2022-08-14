import mysql.connector

def getProductsInfo():
    connection = mysql.connector.connect(host ="localhost", user = "root",password="12345",database = "node-app")
    myCursor = connection.cursor()
    # sql = "Select COUNT(*) from Products"
    sql = "Select AVG(price) from Products"
    sql = "Select SUM(price) from Products"
    sql = "Select MAX(price) from Products"
    sql = "Select MIN(price) from Products"
    sql = "Select Name,Price from Products where price=(Select MAX(price) from Products)"
    
    
    
    myCursor.execute(sql)

    result = myCursor.fetchone()
    print(f"Result  {result[0]}+ {result[1]}")

getProductsInfo()