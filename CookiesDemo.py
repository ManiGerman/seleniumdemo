from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")
#capture all the cookies created by browser

cookies=driver.get_cookies()
print(len(cookies))

print(cookies)

#Adding new cookie to the browser

cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#Deleting cookie
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies))

#Deleting all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))