import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Class will execute only 1 before the test")

    @classmethod
    def tearDownClass(cls):
        print("teardown class will execute after all the test")

    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")