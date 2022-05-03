import unittest
from DemoExample import Sample1


class MyTestCase(unittest.TestCase):
    def test_addingnumbers(self):
        Sample1.add(7,7)

    def test_subNumber(self):
        Sample1.sub(7,4)




#if __name__ == '__main__':
#    unittest.main()
