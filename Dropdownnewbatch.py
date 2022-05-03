import select
import selectors
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
time.sleep(2)
element = driver.find_element(By.XPATH,"//select[@id='RESULT_RadioButton-9']")

drp=Select(element)
print(len(drp.options))


# Count Number of options
