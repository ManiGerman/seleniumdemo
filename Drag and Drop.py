from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element=driver.find_element(By.ID, "box5")
target_element=driver.find_element(By.ID, "box102")

actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()