# When frames are present in the Webpage the selemium driver cannot automatically find it even though the entered locator is correct
# soo make sure to check if the parent of the locator is a frame or not
# The frame will usually be specified with tag names frames or iframe or frameset
import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
#here the switch to frame works with frame ID, frame name or index value
time.sleep(4)
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("PORT")
driver.switch_to.default_content()
#this is used to move the driver back from the frame to html
print(driver.find_element_by_tag_name("h3").text)
driver.close()
