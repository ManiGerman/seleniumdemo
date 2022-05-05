from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")

driver.find_element(By.XPATH, "//*[@id='treemenu']/li/ul/li[1]").click()
driver.find_element(By.XPATH, "//*[@id='treemenu']/li/ul/li[1]/ul/li[4]/a").click()

element=driver.find_element(By.ID, "select-demo")
drp=Select(element)

#drp.select_by_visible_text("Friday")
#drp.select_by_index(6)
drp.select_by_value("Saturday")

print(len(drp.options))

options=drp.options

for option in options:
    print(option.text)
