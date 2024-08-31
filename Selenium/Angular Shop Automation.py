import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
#Mobiles = driver.find_elements_by_css_selector("button[class*='info']")
Phones = driver.find_elements_by_xpath("//div[@class='card h-100']")
for phone in Phones:
    phone_names = phone.find_element_by_xpath("div/h4/a").text
    if phone_names == "Blackberry":
        phone.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_xpath("//input[@id='country']").send_keys("In")
countries = driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
print(len(countries))
for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
result = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
assert "Success" in result
driver.get_screenshot_as_file("result.png")
driver.close()

#//div[@class='card h-100']/div[2]/button