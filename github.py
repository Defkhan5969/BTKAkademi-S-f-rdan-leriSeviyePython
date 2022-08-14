import requests

class Github:
    def  __init__(self):
        self.api_url='https://api.github.com'
        self.token='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'
    def getUser(self,username):
        response= requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getRepositires(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self,name):
        response = requests.post(self.api_url+'/users/repos?access_token'+ self.token,json = 
        {
           "name":name,
           "description":"This is your first repos",
           "homepage":"https://github.com",
           "private":False,
           "has_issues":True,
           "has_projects":True,
           "has_wiki":True,
           "message":"Merhaba"
           

        })
        return response.json()

github = Github()
while True:
    secim = int(input('1-Find User\n2- Get Repositeries\n3-Create Repository\n4-Exit\nSeciminiz:'))
    if secim == 4:
        break
    else:
        if secim == 1:
            username=input("Kullanıcı Adı: ")
            result = github.getUser(username)
            print('name: {0} public repos: {1} followers: {2}'.format(result['name'],result['public_repos'],result['followers']))

            
        elif secim == 2:
            username=input("Kullanıcı Adınız: ")
            result = github.getRepositires(username)
            for repo in result:
                print(repo['name'])


        elif secim == 3:
            name = input("Repo: ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Yanlış Seçim...")