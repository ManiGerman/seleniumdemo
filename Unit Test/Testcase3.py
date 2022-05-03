import unittest

def setupModule():
    print("setupmodule")
def teardownModule():
    print("teardownmodule")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("open application")

    @classmethod
    def tearDownClass(cls):
        print("close application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid Recharge test")

if __name__ == "__main__":
    unittest.main()
