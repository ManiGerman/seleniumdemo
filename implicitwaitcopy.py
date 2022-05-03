from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://www.saucedemo.com/")

driver.implicitly_wait(10)

assert "Swag Labs" in driver.title

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
