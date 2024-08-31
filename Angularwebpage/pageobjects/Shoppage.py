from selenium.webdriver.common.by import By

from pageobjects.checkoutpage import Checkout


class Shoppage:
    def __init__(self, driver):
        self.driver = driver

    value_phone = (By.XPATH, "//div[@class='card h-100']")
    value_checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def get_value_phone(self):
        return self.driver.find_elements(*Shoppage.value_phone)
        # driver.find_elements_by_xpath("//div[@class='card h-100']")

    def get_value_checkout(self):
        self.driver.find_element(*Shoppage.value_checkout).click()
        # self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
        checkout = Checkout(self.driver)
        return checkout
