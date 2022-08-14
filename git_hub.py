from githubUserInfo import username,password
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

class Github:
    def __init__(self,username,passwrod):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.browser.maximize_window()
        self.repositories = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        password = self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)
        time.sleep(1)

        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[12]").click()
    def getRepositiries(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(2)

        items = self.browser.find_elements(By.XPATH,"//*[@id='user-repositories-list']")

        for i in items:
            self.repositories.append(i.find_element(By.XPATH,"//*[@id='user-repositories-list']/ul/li[1]/div[1]/div[1]/h3/a").text)
             

github = Github(username,password)
github.signIn()
github.getRepositiries()
print(github.getRepositiries())
        
        