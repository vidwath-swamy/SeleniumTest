from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
for check in checkbox:
    if check.get_attribute("value") == "option2":
        check.click()
    #assert check.is_selected() # this tells us if that particular checkbox is selected or not
#driver.close()

