from Utilities.Base import Base


# here there is no need to use the pytest fixture as we are now inheriting the fixture data from the base file
class Test_facebook(Base):
    # All classes that use pytest must start with Test_classname
    def test_login(self):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)

# as we are using the driver object from the confest file, we know that we cannot directly call that object, soo we need to use self.object for all occurance of the object
