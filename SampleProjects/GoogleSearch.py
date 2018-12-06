import unittest
from selenium import webdriver
import time
class GoogleSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\Soumyansh\\PycharmProjects\\SeleniumDemo\\Executables\\geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_searchHelloWorld(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Hello World")
        time.sleep(5)
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)
        self.assertEqual("Hello World - Google Search", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
