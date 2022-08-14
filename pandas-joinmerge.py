import pandas as pd

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName':["Yılmaz","Korkmaz","Çelik","Toprak"]

# }

# order = {
#     'OrderId' : [10,11,12,13],
#     'CustomerId':[1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']

# }

# df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(order,columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how ="inner") #Sadece ortak alanı getir
# result = pd.merge(df_customers,df_orders,how ="left") #Sol tarafı getirde sağ tarafı ortak vars getir
# result = pd.merge(df_customers,df_orders,how ="inner") # Sağ tarafı getirde sol tarafı ortak varsa getir
# result = pd.merge(df_customers,df_orders,how ="inner") # Herşeyi getir
# print(result)

customersA = {
     'CustomerId': [1,2,3,4],
     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
     'LastName':["Yılmaz","Korkmaz","Çelik","Toprak"]

}
customersB = {
     'CustomerId': [4,5,6,7],
     'FirstName': ["Zekeriyya","Yağmur","Selçuk","Hakan"],
     'LastName':["Yurt","Korkmaz","Özdemir","Toprak"]

}

df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB],axis=1)

print(result)