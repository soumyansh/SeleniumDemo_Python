from selenium import webdriver
import time
import unittest
from POM.Pages.LoginPage import LoginPage
from POM.Pages.HomePage import HomePage
class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\Soumyansh\\PycharmProjects\\SeleniumDemo\\Executables\\geckodriver.exe");
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        login=LoginPage(self.driver)
        login.enter_username_password("Admin","admin123")
        login.click_login()
        time.sleep(3)
        homepage=HomePage(self.driver)
        homepage.Logout_function()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
