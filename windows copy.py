from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")


driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/a/img").click()

print(driver.current_window_handle)  #parent

handles=driver.window_handles #return all the values of opened browser

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Cross Browser Testing Tool: 2050+ Real Browsers & Devices":
          driver.close()
