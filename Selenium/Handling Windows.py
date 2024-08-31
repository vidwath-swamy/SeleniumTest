from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.find_element_by_tag_name("h3").text)
# Use find element by tagname only when the tagname is Unique
driver.find_element_by_link_text("Click Here").click()
#ChildWindow = driver.window_handles[1]
# The method window_handles stores all the windows opened in a list format, the parent always being at the index[0] position
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element_by_tag_name("h3").text)
driver.quit()
