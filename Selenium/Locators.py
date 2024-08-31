from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\driver\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Port")
driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]").send_keys("port") #using CSS selector
driver.find_element_by_name("email").send_keys("Port.xyz")
driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//label[contains(text(),'Student')]").click()
#driver.find_element_by_id("exampleFormControlSelect1").click("Female")
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)
# while using find element by class make sure you specify only one attribute, as class has multiple attributes separted by space
#.text keyword is used to grab the text from the needed field
driver.find_element_by_css_selector("div[class*=alert]")
#while using the css selector, we can even just use the partial text of the object by using the (*=) operator
#which specifies it as a subtext in the large text
driver.find_element_by_xpath("//div[contains(@class,'alert')]")
#while using the xpath, we can even just use the partial text of the object by using the syntax (//tagname[contains(@attribute,'Value')] operator or (//*[contains(@attribute,'value')] we used the star here instead of specifying the tagname
#which specifies it as a subtext in the large text
driver.close()




# Important!!
# CSS works the fastest in finding the objects, try and use this a lot if you want the code to be well optimized and fast
