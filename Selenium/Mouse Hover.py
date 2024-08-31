import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver =webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#driver.maximize_window()
time.sleep(3)
hover = ActionChains(driver)
# the ActionChains is a package that needs to be called in order to import methods for moving the courser
hover.move_to_element(driver.find_element_by_css_selector("#mousehover")).perform()
# move_to_element method is used to handle the courser
# Make sure to use the .perform method at the end after ever move to element method inorder to perform the specific command
hover.move_to_element(driver.find_element_by_partial_link_text("Top")).click().perform()
time.sleep(2)
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert driver.find_element_by_id("displayed-text").is_displayed()

