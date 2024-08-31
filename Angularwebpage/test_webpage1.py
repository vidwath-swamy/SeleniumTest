import time

import pytest

from Base import Base
from TestData.HomePageData import Data
from pageobjects.Homepage import Homepage


class TestAngular(Base):
    # here instead of using fixture we are inheriting the fixture from base class by passing it as a argument to the class
    def test_page1(self, web_browser, homepagedata):
        log = self.log()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        print(self.driver.title)
        homepage = Homepage(self.driver)
        log.info("Name is " + homepagedata["name"])
        # shoppage = Shoppage(self.driver)  we are now creating this on the homepage class itself
        # checkout = Checkout(self.driver)  we are now creating this on the shoppage class itself
        # location = Location(self.driver) we are now creating this on the checkoutpage class itself
        homepage.get_value_name().send_keys(homepagedata["name"])
        homepage.get_value_email().send_keys(homepagedata["mailid"])
        homepage.get_value_password().send_keys(homepagedata["password"])
        homepage.get_value_checkbox1().click()
        genders = homepage.get_value_gender()
        for gender in genders:
            print(gender.text)
            if gender.text == homepagedata["Gender"]:
                gender.click()
                break
        homepage.get_value_radio2().click()
        homepage.get_value_bady().send_keys("08081996")
        homepage.get_submit().click()
        prompt = homepage.get_alert().text
        assert "Success" in prompt
        shoppage = homepage.get_shop()
        Phones = shoppage.get_value_phone()
        for phone in Phones:
            phone_names = phone.find_element_by_xpath("div/h4/a").text
            log.info(phone_names)
            if phone_names == "Blackberry":
                phone.find_element_by_xpath("div[2]/button").click()
        checkout = shoppage.get_value_checkout()
        location = checkout.get_value_checkout()
        location.get_value_location().send_keys("In")
        time.sleep(5)
        countries = location.get_value_countries()
        print(len(countries))
        print()
        for country in countries:
            if country.text == "India":
                country.click()
                break
        location.get_value_checkbox().click()
        location.get_value_submit().click()
        result = location.get_value_alert().text
        assert "Success" in result
        self.driver.get_screenshot_as_file("result.png")
        self.driver.refresh()
        # this refresh method will refresh the browser once each data set is executed

    # we are using this fixture to send all the data for the homepage screen instead of sending it at each webdriver
    @pytest.fixture(params=Data.test_home_page_data)
    # as we have 2 different datasets here this will execute twice
    def homepagedata(self, request):
        return request.param
