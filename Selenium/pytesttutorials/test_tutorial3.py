# fixtures
# fixtures are like pre-requsites/reports that will be performed before or after the test execution
import pytest


@pytest.fixture()
def test_setup():
    print("ill be printed first")
    yield # the yeild method is used to separate a method into prerequsite and teardown(it will be executed at end)
    print("ill be printed last")


def test_setup1(test_setup): # here we are passing the fixture as a parameter so that it will be execute first
    print("ill be printed second")



