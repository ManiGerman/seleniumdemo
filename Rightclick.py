from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button=driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

actions=ActionChains(driver)

actions.context_click(button).perform()
