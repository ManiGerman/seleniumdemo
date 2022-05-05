from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://leafground.com/pages/frame.html")

driver.switch_to.frame(1)
driver.find_element(By.XPATH, "//button[@id='Click']").click()

time.sleep(2)
driver.switch_to.frame(1)
driver.find_element(By.XPATH, "//button[@id='Click1']").click()
time.sleep(3)

#driver.switch_to.default_content()

#driver.switch_to.frame("packageFrame")  #second frame
#driver.find_element(By.LINK_TEXT, "WebDriver").click()
#time.sleep(3)

#driver.switch_to.default_content()

#driver.switch_to.frame("classFrame") # third frame
#driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
