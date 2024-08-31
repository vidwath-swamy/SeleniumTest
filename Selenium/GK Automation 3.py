# go to flight booking and try to search for a flight
import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_link_text("Flight Booking").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_css_selector("input[value='RoundTrip']").click()
driver.find_element_by_name("ctl00_mainContent_ddl_originStation1_CTXT").send_keys("da")
origin_countries = driver.find_elements_by_xpath("//div[@class='search_options_menucontent']/div/div/ul/li/a")
time.sleep(2)
for origin_country in origin_countries:
    if origin_country.text == "Dhaka (DAC)":
        origin_country.click()
        break
driver.find_element_by_name("ctl00_mainContent_ddl_destinationStation1_CTXT").send_keys("ba")
destination_countries = driver.find_elements_by_xpath("//div[@class='search_options_menucontent']/div/div/ul/li/a")
time.sleep(2)
for destination_country in destination_countries:
    if destination_country.text == "Bangkok (BKK)":
        destination_country.click()
        break
calendar = driver.find_elements_by_css_selector("table[class='ui-datepicker-calendar'] tbody td a")
time.sleep(2)
for date in calendar:
    if date.text == "20":
        date.click()
        break
driver.find_element_by_name("ctl00$mainContent$view_date2").click()
calendar2 = driver.find_elements_by_css_selector("table[class='ui-datepicker-calendar'] tbody td a")
for date1 in calendar2:
    if date1.text == "25":
        date1.click()
        break
driver.find_element_by_css_selector("#divpaxinfo").click()
time.sleep(2)
driver.find_element_by_css_selector("#divChild div:nth-child(2) span:nth-child(3)").click()
driver.find_element_by_css_selector("#divChild div:nth-child(2) span:nth-child(3)").click()
driver.find_element_by_css_selector("#btnclosepaxoption").click()
driver.find_element_by_css_selector("#ctl00_mainContent_DropDownListCurrency").click()
currency = driver.find_elements_by_css_selector("#ctl00_mainContent_DropDownListCurrency option")
for value in currency:
    if value.text == "USD":
        value.click()
        break
driver.find_element_by_css_selector("#ctl00_mainContent_chk_Unmr").click()
driver.find_element_by_css_selector("#ctl00_mainContent_btn_FindFlights").click()
driver.quit()

