import time
import HtmlTestRunner
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://automationpractice.com/")
        cls.driver.maximize_window()

    def test_a_login(self):
       self.driver.find_element(By.LINK_TEXT,'Sign in').click()
       self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("manikandan.a@theswipewire.com")
       self.driver.find_element(By.XPATH,"//input[@id='passwd']").send_keys("test1!")
       self.driver.find_element(By.XPATH,"//button[@id='SubmitLogin']/span").click()
       time.sleep(5)

    def test_b_Cart(self):
        self.driver.find_element(By.LINK_TEXT,'Women').click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,900)", "")
        image=self.driver.find_element(By.XPATH,"//*[contains(@title, 'Blouse')]")
        cart=self.driver.find_element(By.XPATH, "//*[contains(@title, 'Add to cart')]")

        actions=ActionChains(self.driver)
        actions.move_to_element(image).move_to_element(cart).click().perform()

    def tearDownclass(cls):
        time.sleep(10)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Manigandan/PycharmProjects/selenium/Reports'),verbosity=2)