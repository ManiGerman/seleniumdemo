import XLutils


from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://www.saucedemo.com/")

path="C:\Excel data/logins.xlsx"

rows=XLutils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLutils.readData(path,"Sheet1",r,1)
    password=XLutils.readData(path,"Sheet1",r,2)

    driver.find_element(By.ID, "loginUser").send_keys("manikandan.a@buzzwallet.in")
    driver.find_element(By.ID, "loginPassword").send_keys("Germany7&")

    driver.find_element(By.ID,"kt_login_signin_submit").click()
    if driver.title=="Admin-OTP":
        print("Pass")
        XLutils.writeData(path,"sheet1",r,3,"pass")
    else:
        print("Fail")
        XLutils.writeData(path, "sheet1", r, 3, "Fail")

    driver.find_element(By.LINK_TEXT,"https://test.buzzwallet.live/public/images/logos/1605178636_logo.png").click()

