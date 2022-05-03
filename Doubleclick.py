from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

Element=driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)

actions.double_click(Element).perform()