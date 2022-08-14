
from instagamUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.username = username
        self.password = password
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.browser = webdriver.Chrome('chromedriver.exe',options=self.options,chrome_options=self.browserProfile)

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(2)
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

        
        

    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}")
        
    def followUsers(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        
        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text!="Following":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takip ediyorsun")

    def unfollowUsers(self,username):
        self.browser.get("https://www.instagram.com/"+username)

        time.sleep(2)

        followButton = followButton = self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_lN']/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button/div/div")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,"//button[text()='UnFollow']").click()

        
instagram=Instagram(username,password)
instagram.signIn()
# instagram.getFollowers()
instagram.followUsers("engindemirog")

# instagram.unfollowUsers("engindemirog")