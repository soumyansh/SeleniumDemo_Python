import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Firefox(executable_path="C:\\Users\\Soumyansh\\PycharmProjects\\SeleniumDemo\\Executables\\geckodriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")
    yield
    driver.close()
    driver.quit()

def test_login(test_setup):

    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()


def test_demo2(test_setup):
    print("Hi")

