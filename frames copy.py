from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame") #first frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")  #second frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame") # third frame
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
