from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
driver.maximize_window()


rows=len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr"))
cols=len(driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th"))

print(rows)
print(cols)

print("COMPANY"+"      "+"CONTACT"+"           "+"COUNTRY")

for r in range(2,rows+1):
    for c in range(1,cols+1):
      value=driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
      print(value,end='       ')
    print()


