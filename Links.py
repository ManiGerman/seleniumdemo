from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")

links=driver.find_elements(By.TAG_NAME,"a")

print("Total links are:",len(links))

for link in links:
    print(link.text)