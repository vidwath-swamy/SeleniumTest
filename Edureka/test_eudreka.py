from Base import Base
from Pageobjects.Homepage import Homepage
from conftest import Web_Browser_Initialization

class Edureka(Base):
    def test_website_launch(self, Web_Browser_Initialization):
        self.driver.get("https://www.edureka.co/")
        print(self.driver.title)
        assert "Edureka" in self.driver.title

    def test_HomepageLogin(self):
        homepage = Homepage(self.driver)
        homepage.get_value_login().click()
