from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://fs25.formsite.com/bld/FormSite?FormId=LoadCreateNewForm")

inputboxes= driver.find_elements(By.CLASS_NAME, "auth-form__text-input")

print(len(inputboxes))

driver.find_element(By.ID, 'UserId').send_keys("Manikandan.a@thebuzzwallet.in")
driver.find_element(By.ID, 'Password').send_keys("Mallika1!")

driver.find_element(By.ID, 'login').click()
time.sleep(5)
