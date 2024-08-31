from selenium.webdriver.common.by import By
from pageobjects.Shoppage import Shoppage


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    value_name = (By.CSS_SELECTOR, "input[name='name']")
    value_email = (By.CSS_SELECTOR, "input[name='email']")
    value_password = (By.CSS_SELECTOR, "input[type='password']")
    value_checkbox1 = (By.CSS_SELECTOR, "#exampleCheck1")
    value_gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1 option")
    value_radio2 = (By.ID, "inlineRadio2")
    value_bday = (By.CSS_SELECTOR, "input[name='bday']")
    value_submit = (By.CSS_SELECTOR, "input[type='submit']")
    value_alert = (By.CLASS_NAME, "alert")
    value_shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def get_value_name(self):
        return self.driver.find_element(*Homepage.value_name)
        # self.driver.find_element_by_css_selector("input[name='name']")
        # we need to add a * to the class name so that it treats it as a tuple and deserializes it as driver.find_element_by_css_selector("input[name='name']")

    def get_value_email(self):
        return self.driver.find_element(*Homepage.value_email)
        # driver.find_element_by_css_selector("input[name='email']")

    def get_value_password(self):
        return self.driver.find_element(*Homepage.value_password)
        # driver.find_element_by_css_selector("input[type='password']")

    def get_value_checkbox1(self):
        return self.driver.find_element(*Homepage.value_checkbox1)
        # driver.find_element_by_css_selector("#exampleCheck1")

    def get_value_gender(self):
        return self.driver.find_elements(*Homepage.value_gender)
        # driver.find_elements_by_css_selector("#exampleFormControlSelect1 option")

    def get_value_radio2(self):
        return self.driver.find_element(*Homepage.value_radio2)
        # driver.find_element_by_id("inlineRadio2")

    def get_value_bady(self):
        return self.driver.find_element(*Homepage.value_bday)
        # driver.find_element_by_css_selector("input[name='bday']")

    def get_submit(self):
        return self.driver.find_element(*Homepage.value_submit)
        # driver.find_element_by_css_selector("input[type='submit']")

    def get_alert(self):
        return self.driver.find_element(*Homepage.value_alert)
        # driver.find_element_by_class_name("alert")

    def get_shop(self):
        self.driver.find_element(*Homepage.value_shop).click()
        # driver.find_element_by_css_selector("a[href*='shop']")
        # here we are determining which class links the two pages and then perform the click/submit operation here itself, we can even declare the object creation for the next class here itself
        shoppage = Shoppage(self.driver)
        return shoppage
