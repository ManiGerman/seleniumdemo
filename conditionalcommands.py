from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://www.saucedemo.com/")

user_ele=driver.find_element(By.ID, "user-name")

print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element(By.ID, "password")

print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

time.sleep(5)


user_ele.send_keys("standard_user")
pwd_ele.send_keys("secret_sauce")

driver.find_element(By.XPATH, "//*[@id='login-button']").click()

time.sleep(25)


