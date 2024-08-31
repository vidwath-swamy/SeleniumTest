# this file can imported and used instead of user manually defining the fixture in each and every file
# this file MUST be of the name conftest.py only in order for it to work
# when created this file can be used across every pytest test case in a directory
import pytest

#here if i pass scope="class" as an argument for the fixture then it will run the fixture at the class level instead of functional level
# EG: @pytest.fixture(scope="class")
@pytest.fixture()
def setup():
    print("Run this first before every testcase")
    yield
    print("Run this after every testcase")


@pytest.fixture()
def data():
    print("Sending first and last name")
    return ["vidwath", "Swamy"]


@pytest.fixture(params=["vidwath","swamy","Port"])
def test_multiplenames(request):
    # pass the request as a argument only when you are using parameters in the fixture
    return request.param

