from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
chrome_driver_path = "C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)

driver.implicitly_wait(10)
driver.get("https://flippingbook.com/")

links=driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links:
    r = requests.head(link.get_attribute('href')
    if r.status_code!=200:
       driver.get(link)
    else:
        print(str(link) + " isn't available.")