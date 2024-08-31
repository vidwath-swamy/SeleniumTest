import pytest


@pytest.mark.smoke
def test_hello():
    X = 1
    assert X == 2, "error in condition"
