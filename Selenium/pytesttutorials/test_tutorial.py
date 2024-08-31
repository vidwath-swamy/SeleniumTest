# All pytest files should always start or end with test_ followed by file name
# The program that's being tested should always be in a function
# The function created should always start with (test_function name) this is to help pytest recognize the function
# Make sure that all the method names are relevant to the project
# We can even group functions into a selected test run, when we want to run only smoke or regression testcases using the keyword @pytest.mark
import pytest


@pytest.mark.smoke
def test_loginflow():
    print("Hello")


@pytest.mark.skip
def test_hello():
    X = "hello"
    assert X == 2, "error in condition"


