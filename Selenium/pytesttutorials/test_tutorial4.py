import pytest


@pytest.mark.usefixtures("data")
class Test_Example1:
    def test_name(self, data):
        print(data)
    # we can even print individual elements in the tuple using
        print(data[1])
