from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a").click()
time.sleep(5)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium.chrome").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "ChromeDriver").click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")

driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
time.sleep(3)


