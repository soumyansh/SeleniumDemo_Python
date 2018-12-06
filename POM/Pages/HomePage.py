import time
from POM.Locators.PageLocators import locators
class HomePage():

    def __init__(self,driver):
        self.driver=driver
        self.welcome_id=locators.welcome_id
        self.logout_xpath=locators.logout_xpath

    def Logout_function(self):
        self.driver.find_element_by_id(self.welcome_id).click()
        self.driver.find_element_by_xpath(self.logout_xpath).click()
        time.sleep(3)
