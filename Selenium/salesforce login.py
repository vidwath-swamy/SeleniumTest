import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path = "E:\driver\chromedriver.exe")
driver.get("https://login.salesforce.com/")
print(driver.title)
driver.find_element_by_css_selector("#username").send_keys("port@mail.com")
#driver.find_element_by_css_selector(".password").send_keys("12345")
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)
#driver.find_element_by_name("rememberUn").click()
#driver.find_element_by_id("Login").click()
#print(driver.find_element_by_id("error").text)
#driver.find_element_by_link_text("Forgot Your Password?").click()
#time.sleep(10)
#driver.find_element_by_name("cancel").click()
#driver.close()