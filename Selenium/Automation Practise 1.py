# select everything from this webpage
# retrieve or add items listed in the tables
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.implicitly_wait(5)
List1 = []
List2 = []
driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")
driver.find_element_by_css_selector("input[value='radio2']").click()
driver.find_element_by_class_name("inputs").send_keys("por")
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] div")
print(len(countries))
for country in countries:
    print(country.text)
    if country.text == "Portugal":
        country.click()
        break
dropdown = driver.find_elements_by_css_selector("select[name='dropdown-class-example'] option")
for item in dropdown:
    if item.text == "Option2":
        item.click()
        break
driver.find_element_by_css_selector("#checkBoxOption2").click()
driver.find_element_by_css_selector("#checkBoxOption3").click()
driver.find_element_by_css_selector("#openwindow").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_css_selector("#opentab").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_css_selector("#name").send_keys("PORT")
driver.find_element_by_css_selector("#confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
prices = driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr/td[3]")
for price in prices:
    List1.append(price.text)
List1 = map(int, List1)
print(sum(List1))
Amounts = driver.find_elements_by_css_selector("div[class='tableFixHead'] tbody tr td:nth-child(4)")
for amount in Amounts:
    List2.append(amount.text)
List2 = map(int, List2)
print(sum(List2))
print(driver.find_element_by_css_selector("#displayed-text").is_displayed())
driver.find_element_by_css_selector("#hide-textbox").click()
print(driver.find_element_by_css_selector("#displayed-text").is_displayed())
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_css_selector("#mousehover")).perform()
actions.move_to_element(driver.find_element_by_partial_link_text("Top")).click().perform()
driver.switch_to.frame("courses-iframe")
wait = WebDriverWait(driver,5)
print(driver.find_element_by_link_text("Mentorship").is_enabled())
frame = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Mentorship")))
# here im getting a element located but click intercepted exception
# Sooo we made use of the execute script method and passed the index of the Argument
driver.execute_script('arguments[0].click()', frame)
#driver.find_element_by_css_selector("div[class='thrv_wrapper thrv_icon tcb-icon-open']").click()
