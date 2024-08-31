import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()
print(driver.title)
driver.find_element_by_css_selector("input[name='username']").send_keys("Port")
driver.find_element_by_css_selector("input[name='pw']").send_keys("12345")
driver.find_element_by_css_selector("input[type='checkbox']").click()
driver.find_element_by_css_selector("#Login").click()
time.sleep(10)
print(driver.find_element_by_css_selector("#error").text)
driver.find_element_by_link_text("Forgot Your Password?").click()
print(driver.find_element_by_css_selector("#header").text)
driver.find_element_by_css_selector("input[name='cancel']").click()
print(driver.title)
driver.close()