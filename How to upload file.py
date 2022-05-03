from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")

driver.maximize_window()

driver.find_element(By.NAME, "upfile").send_keys("C:/Users/Manigandan/Documents/Pic/image.jpg")
