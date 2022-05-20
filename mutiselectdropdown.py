import select
import selectors
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
time.sleep(2)

element=driver.find_element(By.ID,"multi-select")

drp=Select(element)

V=drp.select_by_visible_text("California")
I=drp.select_by_index(3)
V=drp.select_by_value("Florida")
f=drp.deselect_by_value("Florida")

print(len(drp.options))

for option in drp.options:
    print(option.text)