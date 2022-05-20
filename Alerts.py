from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button['text=Click Me']").click()

time.sleep(5)

alert = driver.switch_to.alert

alert.title.accept()

#driver.switch_to.alert.dismiss()