from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://www.saucedemo.com/")

print(driver.title)
print(driver.current_url)
time.sleep(2)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

time.sleep(5)

driver.quit()