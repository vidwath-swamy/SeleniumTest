from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    value_login = (By.CSS_SELECTOR, "span[data-target='#new_sign_up_optim']")

    def get_value_login(self):
        return self.driver.find_element(*Homepage.value_login)
