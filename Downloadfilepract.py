from selenium import webdriver
from selenium.webdriver.chrome.options import Options
ChromeOptions = webdriver.ChromeOptions()
from selenium.webdriver.common.by import By

ChromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:/Users/Manigandan/Pictures/Camera Roll"})

driver=webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe",options=ChromeOptions)

driver.get("https://freetestdata.com/")

driver.maximize_window()


driver.find_element(By.XPATH, "//span[@class='elementor-button-text']").click()


