import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="../Executables/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_searchGoogle_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_xpath("//*[@name='q']").send_keys("Hello World")
        print(self.driver.title)
        self.assertEqual("Google",self.driver.title)
        time.sleep(3)

    def test_searchGoogle_2(self):
        self.driver.get("https://www.google.com")

        self.driver.find_element_by_xpath("//*[@name='q']").send_keys("Hello World again")
        time.sleep(3)
        wait=webdriver(self.driver,10)
        element=wait.until(expected_conditions.element_to_be_selected(By))
        print(self.driver.title)
        self.assertEquals("Google",self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
