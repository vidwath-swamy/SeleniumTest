# Shopping from the website and returning Success once purchase is done
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)
driver.find_element_by_link_text("Shop").click()
product_body = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in product_body:
    product_name = product.find_element_by_xpath("div/h4/a").text
    print(product_name)
    if product_name == "Samsung Note 8":
        product.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
in_cart_name = driver.find_element_by_css_selector("h4[class='media-heading'] a").text
assert "Samsung Note 8" in in_cart_name
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_css_selector("input[id='country']").send_keys("ar")
countries = driver.find_elements_by_css_selector("div[class='suggestions'] ul li a")
for country in countries:
   # print(country.text)
    if country.text == "Denmark":
        country.click()
        break
driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[value='Purchase']").click()
confirmed = driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
assert "Success" in confirmed
driver.close()
