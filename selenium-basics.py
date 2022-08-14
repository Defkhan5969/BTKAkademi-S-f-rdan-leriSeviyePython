from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)
driver.maximize_window()

driver.save_screenshot("github.com-homepage.png")
url = "https://github.com/Defkhan5969"
driver.get(url)
print(driver.title)

if "Defkhan5969" in driver.title:
    driver.save_screenshot("Defkhan5969.png")



time.sleep(2)

driver.back()
time.sleep(2)

driver.close()