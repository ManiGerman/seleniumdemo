from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://demo.seleniumeasy.com/")
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/a/img").click()


print(driver.current_window_handle)

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)



