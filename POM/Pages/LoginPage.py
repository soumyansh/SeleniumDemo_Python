import time
from POM.Locators.PageLocators import locators
class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_name=locators.username_textbox_name
        self.pasword_textbox_name=locators.pasword_textbox_name
        self.login_button_name=locators.login_button_name

    def enter_username_password(self,username,password):
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)
        self.driver.find_element_by_name(self.pasword_textbox_name).send_keys(password)


    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()
        time.sleep(3)