import XLutils
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://accounts.lambdatest.com/login")

path = "C:\\Excel_data\\logins.xlsx"

rows = XLutils.getRowCount(path, 'Sheet1')
for r in range(2, rows):
    username = XLutils.readData(path, "Sheet1", r, 1)
    password = XLutils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    if driver.title=="Welcome - LambdaTest":
        print("Test has been passed")
        XLutils.writeData(path, "Sheet1", r, 3, "pass")
        driver.find_element(By.ID, "profile__dropdown").click()
        time.sleep(2)
        driver.find_element(By.ID, "app__logout").click()
        time.sleep(2)
    else:
        print("Test has been failed")
        XLutils.writeData(path, "Sheet1", r, 3, "fail")
    time.sleep(2)
