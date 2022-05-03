from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://test.buzzwallet.live/")

implicitly_wait(10)

print(driver.title)
print(driver.current_url)