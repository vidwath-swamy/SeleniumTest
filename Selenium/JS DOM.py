# DOM = Document Object Module
# JavaScript DOM can access any element on webpage just like selenium
# Selenium has a method to use JS code in iit
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("PORT")
print(driver.find_element_by_name("name").text)
# ^this returns nothing as selenium will not handle the texts that user enters after loading the page this way
# we need to use
print(driver.find_element_by_name("name").get_attribute("value"))
# We need to use the Get attribute method and pass the value argument to retrieve any data entered after the page has loaded
# But we can also retrieve the data using the DOM Module
# This is the Method needed, and make sure its in single quotes
# use the return statement before the document to return the value to the selenium and then we can print it
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
# The above method is written using only javascript
# use this when none of the Selenium function works
shop_button = driver.find_element_by_css_selector("a[href*='shop']")
# We can even execute javascript this way
# Syntax being arguments[Index position of the value we are passing]. We can even pass the method like click/clear/text anything
driver.execute_script('arguments[0].click()',shop_button)
