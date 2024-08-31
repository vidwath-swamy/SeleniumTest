import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service

@pytest.fixture(scope="class")
def Web_Browser_Initialization():
    global driver
    S = Service("E:/driver/chromedriver.exe")
    driver = webdriver.Chrome(service=S)
