import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.XPATH, "//*[@id='txtUsername']" ).send_keys("Admin")
driver.find_element(By.XPATH, "//*[@id='txtPassword']" ).send_keys("admin123")
driver.maximize_window()

time.sleep(5)

driver.find_element(By.NAME, "Submit").click()


admin=driver.find_element(By.ID, "menu_admin_viewAdminModule")
usermgnt=driver.find_element(By.ID, "menu_admin_UserManagement")
users=driver.find_element(By.ID, "menu_admin_viewSystemUsers")

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()


