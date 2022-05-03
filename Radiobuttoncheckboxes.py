from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
driver.find_element(By.XPATH,"//*[@id='easycont']/div/div[2]/div[1]/div[2]/label[1]/input").click()
status=driver.find_element(By.XPATH,"//*[@id='easycont']/div/div[2]/div[1]/div[2]/label[1]/input").is_selected()
print(status)

driver.find_element(By.XPATH, "//*[@id='treemenu']/li/ul/li[1]").click()
driver.find_element(By.XPATH, "//*[@id='treemenu']/li/ul/li[1]/ul/li[2]/a").click()
driver.find_element(By.ID, "isAgeSelected").click()
