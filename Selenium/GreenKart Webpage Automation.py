from selenium import webdriver
from selenium.webdriver.common.by import By  #used when we are defining a condition with method, see line 23
from selenium.webdriver.support import expected_conditions #used for Explicit Wait only when we want to wait till certain conditions are met
from selenium.webdriver.support.wait import WebDriverWait  # used for Explicit wait only
# Explicit wait is used for targetting any specific step when we feel like that step will take time to execute
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
list1 = []
#driver.implicitly_wait(5)
# The implicit wait a Global Method,
# The implicit wait, waits for a Maximum of X seconds after every method Before returning an error if any
# If the Method returns the Needed values fast then the Script execution will also continue
# it will only wait for the next mention to load for a max of X seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_class_name("search-keyword")#.send_keys("beetroot")
Products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(Products))
Products = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for product in Products:
    product.click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]/button").click()
wait = WebDriverWait(driver, 10)
#Here we are waiting for the Driver for a max of 10 Seconds
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promocode")))
#Here we are defining the Expected condition till when this step should wait, by passing the Locator
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
Total = driver.find_elements_by_xpath("//tr/td[5]/p")
for item in Total:
    list1.append(item.text)
print(list1)
list = map(int, list1)
print(sum(list))
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
driver.close()


