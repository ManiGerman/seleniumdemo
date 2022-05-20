import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")


element=driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-1']").get_attribute("value")

print(element)