from selenium.webdriver.common.by import By

from pageobjects.locationpage import Location


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    value_checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def get_value_checkout(self):
        self.driver.find_element(*Checkout.value_checkout).click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']")
        location = Location(self.driver)
        return location
