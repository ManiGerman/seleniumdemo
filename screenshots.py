from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://accounts.lambdatest.com/login")

driver.save_screenshot("C:\Excel_data\mani.png")

driver.get_screenshot_as_file("C:\Excel_data\hmani2.jpg")