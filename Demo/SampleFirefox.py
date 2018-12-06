import time

from selenium import webdriver


driver=webdriver.Firefox(executable_path="../Executables/geckodriver.exe")


driver.set_page_load_timeout(30);
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Hello world")
time.sleep(5)
driver.quit()
print("Test Completed")
driver.find_element_by_xpath()