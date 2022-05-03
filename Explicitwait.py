import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://automationpractice.com/index.php")

driver.find_element(By.ID,"search_query_top").send_keys("shirt")

driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

