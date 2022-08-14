from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter:
    def __init__(self,username,password):
        self.browseProfile= webdriver.ChromeOptions()
        self.browseProfile.add_experimental_option('pref',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome()
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://twitter.com/login")
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
        
        # self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]").click()
        
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input")
        passwordInput.send_keys(self.password)
        btnSubmit =self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        btnSubmit.click()

        time.sleep(2)
    def search(self, hashtag):
        self.browser.get("https://twitter.com/explore")
        searchInput=self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)

        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        list = self.browser.find_elements(By.XPATH,"//div[@data-testid='cellInnerDiv]/div[2]/div[2]")
        for item in list:
            print(item.text)


twitter=Twitter(username,password)
# twitter.signIn()
twitter.search("python")
    
