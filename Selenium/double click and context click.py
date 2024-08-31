from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
double_click = ActionChains(driver)
double_click.move_to_element(driver.find_element_by_css_selector("#double-click")).context_click().perform()
# this is Right click
double_click.move_to_element(driver.find_element_by_css_selector("#double-click")).double_click().perform()
# this is double click
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element_by_name("prompt").click()
alert_1 = driver.switch_to.alert
alert_1.send_keys("PORTSDad")
print(alert_1.text)
alert_1.accept()
