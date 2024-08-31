#using the Angular Webpage
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.find_element_by_xpath("//div[@class='form-group']/input[@name='name']").send_keys("PORT")
driver.find_element_by_css_selector("div[class='form-group'] input[name='email']").send_keys("port@mail.com")
driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("1234")
driver.find_element_by_css_selector("#exampleCheck1").click()
####Note: Make sure to use the select Method only when the tagname is also select
dropdown = Select(driver.find_element_by_css_selector("#exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female") #using visible text = you need to mention the Text in the Dropdown menu
#dropdown.select_by_index(0) #using Index you can select the value based on the Index it starts with 0
#dropdown.select_by_value() # in some cases the dropdown attributes will have values attached to them, in those cases you can use the value method
driver.find_element_by_css_selector("input[value='option2']").click()
driver.find_element_by_css_selector("input[name='bday']").send_keys("08081996")
driver.find_element_by_css_selector("input[value='Submit']").click()
Test = driver.find_element_by_class_name("alert-success").text
assert "Success!" in Test
driver.close()

