from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path="E:\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window() #used to maximize the window
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window() #used to minimize the window
print(driver.title)
driver.refresh() #this method can be used to refresh the current page
driver.back() # when user navigates to different pages via a url, the back method can be used to get back to
              # the previous# page
driver.close()



