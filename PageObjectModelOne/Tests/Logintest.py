import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner
from selenium.webdriver.common.by import By
from PageObjectModelOne.Pages.Loginpage import LoginPageProp
from PageObjectModelOne.Pages.cartpage import CartPageProp
from PageObjectModelOne.Pages.checkoutpage import CheckoutPageProp

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_a_login(self):
        loginprop = LoginPageProp()
        self.driver.find_element(By.ID, loginprop.username_text_field_id).send_keys("standard_user")
        self.driver.find_element(By.ID, loginprop.password_text_field_id).send_keys("secret_sauce")
        self.driver.find_element(By.ID, loginprop.login_button_id).click()
        time.sleep(2)

    def test_b_cart(self):
        cartprop=CartPageProp()
        self.driver.find_element(By.XPATH, cartprop.shopping_cart_link_xpath).click()
        time.sleep(2)

    def test_c_checkout(self):
        checkoutprop=CheckoutPageProp()
        self.driver.find_element(By.ID,checkoutprop.checkout_button_text_id).click()
        self.driver.find_element(By.ID,checkoutprop.first_name_text_id).send_keys("German")
        time.sleep(10)



    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(Output='C:/Users/Manigandan/PycharmProjects/selenium/Reports'),verbosity=2)
