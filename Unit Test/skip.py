import unittest
class Apptesting(unittest.TestCase):

    @unittest.SkipTest #Decorator
    def test_search(self):
        print("This is search test")
    @unittest.skip("it should skip")
    def test_advancedsearch(self):
        print("This is Advanced search test")
    @unittest.skipIf(1==1,"one not equal")
    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid Recharge test")

    def test_loginbygmail(self):
        print("This is login  by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__ == "__main__":
    unittest.main()
