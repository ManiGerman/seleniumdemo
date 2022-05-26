import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://15.207.247.107/get-started")
        cls.driver.maximize_window()

    def test_a_login(self):
            driver = self.driver
            self.driver.find_element(By.XPATH, "//ion-button[@class='md button button-solid ion-activatable ion-focusable hydrated']").click()
            self.driver.find_element(By.XPATH, "//input[@name='mobile']").send_keys("9094151608")
            self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("jmeter1!")
            self.driver.find_element(By.XPATH, "//ion-button[contains(text(),'hydrated')]").click()
            time.sleep(2)

    def test_b_upcoming(self):
            self.driver.find_element(By.XPATH, "//p[text()='MCC']").click()
            self.driver.find_element(By.XPATH,"//ion-button[@class='btn-create md button button-solid ion-activatable ion-focusable hydrated']").click()
            time.sleep(10)

    # def test_c_checkout(self):
    #         checkoutprop=CheckoutPageProp()
    #         self.driver.find_element(By.ID,checkoutprop.checkout_button_text_id).click()
    #         self.driver.find_element(By.ID,checkoutprop.first_name_text_id).send_keys("German")
    #         time.sleep(10)

    @classmethod
    def tearDownClass(cls):
            time.sleep(5)
            cls.driver.quit()

    if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(Output='C:/Users/Manigandan/PycharmProjects/selenium/Reports'),verbosity=2)
