from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
chrome_driver_path = "C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)

driver.implicitly_wait(10)
driver.get('https://google.co.in/')

links=driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links:
    r = requests.head(link.get_attribute("href"))
    print(link.get_attribute('href'), r.status_code)