from selenium import webdriver
import pytest


# here we are defining an option that the user needs to enter on the command prompt to select the webbrowser in which we need to run the testcase during runtime
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def web_browser(request):
    # we need to pass the request as an instance to the fixture, it is a industry wide used instance
    # as we have now select the browser during runtime we need to call that option here using
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:/driver/geckodriver.exe")
        request.cls.driver = driver
    # with this we can access the driver object on class level(cls.object) throughout all programs using the pytest usefixture command
        yield
        driver.close()

# Now when running the test via cmd line we need to specify the browser also using the additional commands --browser_name chrome/firefox
