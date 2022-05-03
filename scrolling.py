from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0,1000)","")
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

links = driver.find_element(By.XPATH,"//*[@id='PopularPosts1']/div/div/article[1]/h3/a")
driver.execute_script("arguments[0].scrollIntoView();",links)


driver.execute_script("window.scrollyBy(0,500)","  ")

driver.execute_script("argument[0].ScrollIntoView();",Element)


