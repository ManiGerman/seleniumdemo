import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")


driver.execute_script("document.getElementsByName('RESULT_TextField-6')[0].value= 'Manikandan'")

time.sleep(5)