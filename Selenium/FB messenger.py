import time

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
#options.add_argument("--disable-popup-blocking")
# here the experimental options can be set to 1 or 2. 1 being Allow and 2 being Block
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
driver = webdriver.Chrome(executable_path="E:\driver\chromedriver.exe",options=options)
driver.implicitly_wait(5)
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("vidwath.swamy@ptw-intl.org")
driver.find_element_by_css_selector("#pass").send_keys("9343773929")
driver.find_element_by_name("login").click()
#driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
driver.find_element_by_xpath("//div[@aria-label='Messenger']").click()
driver.find_element_by_css_selector("a[aria-label='See all in Messenger']").click()
driver.find_element_by_css_selector("input[placeholder='Search Messenger']").send_keys("Vid")
names = driver.find_elements_by_css_selector("a[role='presentation'] span span span")
for name in names:
    print(name.text)




