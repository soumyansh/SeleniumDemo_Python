import unittest
from Examples import Example


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Prints before every method")
    def tearDown(self):
        print("Prints after every method")

    def test_add(self):
        result=Example.add(self,10,15)

        self.assertEqual(result, 25)
        print("Addition assertion successfull")


    def test_sub(self):
        result=Example.sub(self,10,5)

        self.assertEqual(result, 5)
        print("Subtraction assertion successfull")
    @classmethod
    def setUpClass(cls):
        print("Before all method")
    @classmethod
    def tearDownClass(cls):
        print("After all method")

if __name__ == '__main__':
    unittest.main()
