import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome("C:/Users/Manigandan/Documents/chromedriver_win32/chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebpage=driver.title

        #asserteEqual
        #self.assertEqual("Googlee",titleOfWebpage,"webpage not equal")
        self.assertNotEqual("Google",titleOfWebpage)
if __name__ == "__main__":
    unittest.main()

