# go to TOP deals, increase page size to max and order the fruit name in Ascending order
# total the price and discount
import copy

from selenium import webdriver
List1 = []
List2 = []
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_link_text("Top Deals").click()
driver.switch_to.window(driver.window_handles[1])
page_size = driver.find_elements_by_css_selector("select[id='page-menu'] option")
for size in page_size:
    print(size.text)
    if size.text == "20":
        size.click()
driver.find_element_by_css_selector("th[aria-label='Veg/fruit name: activate to sort column ascending']").click()
Total_Price = driver.find_elements_by_xpath("//table[@class='table table-bordered']/tbody/tr/td[2]")
for price in Total_Price:
    List1.append(price.text)
print(List1)
List1 = map(int, List1)
print(sum(List1))
Discounted_Total = driver.find_elements_by_xpath("//table[@class='table table-bordered']/tbody/tr/td[3]")
for discount in Discounted_Total:
    List2.append(discount.text)
print(List2)
List2 = map(int, List2)
print(sum(List2))
driver.quit()
