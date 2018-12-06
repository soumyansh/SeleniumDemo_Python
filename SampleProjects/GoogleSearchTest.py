from selenium import webdriver
import time
import unittest


driver=webdriver.Firefox(executable_path="C:\\Users\\Soumyansh\\PycharmProjects\\SeleniumDemo\\Executables\\geckodriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Hello World")
time.sleep(5)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()