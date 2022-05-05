import XLutils
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://accounts.lambdatest.com/login")

path = "C:\\Excel_data\\logins.xlsx"

row=XLutils.getRowCount(path,sheetName)

for r in range(2,rows+1)
    uname= XLutils.readData(path,sheet1,r,1)
    pname= XLutils.readData(path,sheet1,r,2)

    driver.find_element(By.Id,uname).send_keys(uname)
    driver.find_element(By.Id,pname).send_keys(pname)

    If driver.title= abc
    result = XLutils.writeData(path,sheet1,r,3)


