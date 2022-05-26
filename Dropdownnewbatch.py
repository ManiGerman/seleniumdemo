import select
import selectors
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
# time.sleep(2)
# element = driver.find_element(By.XPATH,"//select[@id='RESULT_RadioButton-9']")
#
# drp=Select(element)
# print(len(drp.options))
driver.get("http://15.207.247.107/get-started")
driver.find_element(By.XPATH, "//*[@id='main']/app-get-started/ion-content/ion-grid/div[2]/ion-button").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']").send_keys("9094151608")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("jmeter1!")
driver.find_element(By.XPATH, "//ion-button[contains(text(),'hydrated')]").click()
time.sleep(2)



driver.find_element(By.XPATH,"//p[text()='MCC']").click()
driver.find_element(By.XPATH,"//ion-button[@class='btn-create md button button-solid ion-activatable ion-focusable hydrated']").click()

# Count Number of options
