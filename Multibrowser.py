from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.30.0-win64\geckodriver.exe")

#driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.9.0\IEdriverserver.exe")

driver.get("https://test.buzzwallet.live/")

print(driver.title)

print(driver.current_url)

driver.close()