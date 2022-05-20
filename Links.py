from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")

links=driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links:
    print(link.text)