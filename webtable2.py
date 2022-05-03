from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()

rows=len(driver.find_elements(By.XPATH,"//*[@id='countries']/tbody/tr"))
cols=len(driver.find_elements(By.XPATH,"//*[@id='countries']/tbody/tr[1]/td"))

print(rows)
print(cols)

print("Visited" +"    "+"Country"+"     "+"Capital(s)"+"       "+"Currency"+"    "+"     "+"Primary Language(s)")


for r in range(2,rows+1):
    for c in range(1,cols+1):
      Value=driver.find_element(By.XPATH, "//*[@id='countries']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
      print(Value,end='    ')
    print()

