# Selenium doesnt support scrolling operation
# soo we need to use Java Script function
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script('arguments[0].click()',shop_button)
# use this method to scroll through the webpage
# the syntax of this is window.scrollTo(horizontal value, vertical value)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
