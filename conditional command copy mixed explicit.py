from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.implicitly_wait(5)

driver.get("http://webdriveruniversity.com/index.html")

driver.get("http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

wait=WebDriverWait(driver,10)

element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='checkboxes']/label[1]/input")))

element.click()
