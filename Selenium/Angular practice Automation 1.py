# Automation to fill up the form and return true if success

from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("PORT")
driver.find_element_by_name("email").send_keys("123@123.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
driver.find_element_by_css_selector("input[type='checkbox']").click()
genders = driver.find_elements_by_css_selector("select[id='exampleFormControlSelect1'] option")
for gender in genders:
    print(gender.text)
    if gender.text == 'Female':
        gender.click()
driver.find_element_by_css_selector("input[value='option1']").click()

driver.find_element_by_css_selector("input[type='submit']").click()
alert = driver.find_element_by_class_name("alert").text
assert "Success!" in alert
#driver.close()
