import unittest
from selenium import webdriver

class newone(unittest.TestCase):
  def test_newone(self):
    self.driver=webdriver.chrome(executable_path="   ")
    self.driver.get("www.google.com")
    print("Title of the page is : self.driver.title")
    self.driver.close()

  def test_secondone(self):
    self.driver=webdriver.chrome(executable_path="   ")
    self.driver.get("www.google.com")
    print("Title of the page is : self.driver.title")
    self.driver.close()



if __name__ == "__main__":
    unittest.main)()