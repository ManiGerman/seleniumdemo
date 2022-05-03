from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://www.saucedemo.com/")

print(driver.title)
time.sleep(5)
driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)

print(driver.title)
driver.back()

time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)

print(driver.title)