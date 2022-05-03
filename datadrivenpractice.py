import XLutils

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
path="C:/Users/Manigandan/Documents/Selenium/Jmeter.xlsx"

rows=XLutils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    username=XLutils.readData(path,"Sheet1",r,1)
    password=XLutils.readData(path,"Sheet1",r,2)

    driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@id='passwd']").send_keys(password)

    driver.find_element(By.XPATH,"//*[@id='SubmitLogin']/span").click()

    if driver.title=="My account - My Store":
       print("Passed")
       XLutils.writeData(path,"Sheet1",r,3,"Passed")

    else:
        print("FAILED")
        XLutils.writeData(path, "Sheet1", r, 3, "Failed")

    driver.find_element(By.PARTIAL_LINK_TEXT,'out').click()



