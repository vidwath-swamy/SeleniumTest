import pytest


@pytest.mark.usefixtures("setup")
class Test_Example:

    def test_test1(self):
        print("this is test1")

    def test_test2(self):
        print("this is test2")

    def test_test3(self):
        print("this is test3")

    def test_test4(self):
        print("this is test4")