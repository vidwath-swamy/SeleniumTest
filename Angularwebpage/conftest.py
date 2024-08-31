from selenium import webdriver
import pytest
driver = None

# here we are defining an option that the user needs to enter on the command prompt to select the webbrowser in which we need to run the testcase during runtime
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def web_browser(request):
    global driver
    # we need to pass the request as an instance to the fixture, it is a industry wide used instance
    # as we have now select the browser during runtime we need to call that option here using
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
    elif browser_name =="firefox":
        driver = webdriver.Firefox(executable_path="E:/driver/geckodriver.exe")
    request.cls.driver = driver
    # with this we can access the driver object on class level(cls.object) throughout all programs using the pytest usefixture command
    yield
    driver.close()

# this is used to add a screenshot to the report whenever any of the testcases fail
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

# Now when running the test via cmd line we need to specify the browser also using the additional commands --browser_name chrome/firefox