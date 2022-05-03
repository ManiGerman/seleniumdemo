import unittest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromrDriverManager

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(chromrDriverManager().install())
        cls.driver.get("https://fs25.formsite.com/bld/FormSite?FormId=LoadCreateNewForm")
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.find_element(By.ID, 'UserId').send_keys("Manikandan.a@thebuzzwallet.in")
        self.driver.find_element(By.ID, 'Password').send_keys("Mallika1!")
        self.driver.find_element(By.ID, 'login').click()
        time.sleep(40)

    def test_createAccount(self):
        drp_element = driver.find_element(By.ID, 'select-folder')
        drp = Select(drp_element)
        drp.select_by_visible_text('New Folder...')

    @classmethod
    def tearDownClass(cls):
        time.sleep((5)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()