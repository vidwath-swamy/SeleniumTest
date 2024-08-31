import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("#autosuggest").send_keys("Ind")
time.sleep(5)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
a = driver.find_element_by_css_selector("#autosuggest").get_attribute('value')
#this get arrtibute method is used to return any changes in the webpage after the page is loaded
assert "India" in a
#^here we are verifying that the Search area indeed has the new Value India
driver.close()

