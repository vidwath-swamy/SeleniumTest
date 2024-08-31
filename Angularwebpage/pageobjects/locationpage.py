from selenium.webdriver.common.by import By


class Location:
    def __init__(self, driver):
        self.driver = driver

    value_location = (By.XPATH, "//input[@id='country']")
    value_countries = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    value_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    value_submit = (By.XPATH, "//input[@type='submit']")
    value_alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def get_value_location(self):
        return self.driver.find_element(*Location.value_location)
        #driver.find_element_by_xpath("//input[@id='country']")

    def get_value_countries(self):
        return self.driver.find_elements(*Location.value_countries)
        #.driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")

    def get_value_checkbox(self):
        return self.driver.find_element(*Location.value_checkbox)
        #driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")

    def get_value_submit(self):
        return self.driver.find_element(*Location.value_submit)
        #self.driver.find_element_by_xpath("//input[@type='submit']")

    def get_value_alert(self):
        return self.driver.find_element(*Location.value_alert)
        #driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']")
