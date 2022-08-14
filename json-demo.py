
import json

class User:#Kullanıcı tanımlar
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email


class UserRepository: #Kullanıcı yönet
    def __init__(self):
        self.users= []
        self.isLoggedIn=False
        self.currentUser = {}

        #load users from .json file
        self.loadUser()
    def loadUser(self):
        pass
    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu")

        
    def login(self):
        pass
    def savetoFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            json.dump(list,file)

repositor = UserRepository()
while True:
    print("Menü".center(50,"*"))
    secim = input('1- Register\n 2- Login \n3- Log Out\n 4- identity\n 5- Exit \n Seçiminiz: ')
    if int(secim)==5:
        break
    else:
        if secim =='1':
            username=input("Username")
            password=input("Password")
            email=input("E-Mail")
            user=User(username=username,password=password,email=email)
            repositor.register(user)

            print(repositor.users)
        elif secim=='2':
            pass#log in
        elif secim=='3':
            pass #log out
        elif secim=='4':
            pass #identity
        else:
            print("Yanlış Seçim")