from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:/Users/Manigandan/Documents/File"})
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element(By.ID,"textbox").send_keys("Testing")

driver.find_element(By.XPATH, "//*[@id='createTxt']").click()
driver.find_element(By.ID, "link-to-download").click()
