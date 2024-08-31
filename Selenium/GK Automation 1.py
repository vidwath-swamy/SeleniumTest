# 1. Checking if the item selected in Page 1 are shown in page 2
# 2. Checking if the Price Decreases when discount is applied
# 3. Verify if the Sum of products matches with the total Amount

# Task 1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


List1 = []
List2 = []
List3 = []
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ca")
time.sleep(3)
Products = driver.find_elements_by_xpath("//div[@class='product-action']")
for product in Products:
    #List1.append(product.find_elements_by_xpath("parent::div/parent::div/h4").text)
    product.click()
a = driver.find_elements_by_css_selector("h4[class='product-name']")
print(len(a))
for productname in a:
    List1.append(productname.text)
print(List1)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promocode")))
b = driver.find_elements_by_xpath("//p[@class='product-name']")
for product_name in b:
    List2.append(product_name.text)
print(List2)
assert List2 == List1

print("Element matches")

# Task 2
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button[class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
Total_Amount = driver.find_element_by_css_selector("span[class='totAmt']").text
print(Total_Amount)
Total_after_discount = driver.find_element_by_css_selector("span[class='discountAmt']").text
assert Total_after_discount < Total_Amount
print("Yes, the Price decreases after discount and the current total is ==", Total_after_discount)

#Task 3
Costs = driver.find_elements_by_xpath("//tr/td[5]/p")
for cost in Costs:
    List3.append(cost.text)
converted_list = list(map(int, List3))
print(List3)
print(converted_list)
print(sum(converted_list))
assert sum(converted_list) == int(Total_Amount)
print("Success")
driver.close()





