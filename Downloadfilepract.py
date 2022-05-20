from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_experimental_option("prefs",{"download.default_directory" : "C:\\Users\\Manigandan\\PycharmProjects\\selenium\\download"})
driver=webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe",options=ChromeOptions)


driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div[1]/a").click()

