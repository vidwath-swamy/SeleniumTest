from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("PORT")
driver.find_element_by_css_selector("#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
text = alert.text
a = "PORT"
assert a in text
alert.accept()
