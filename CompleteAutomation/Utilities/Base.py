# here we will declare all the base classes which can be used in any of the programs so that the code looks cleaner
import pytest

# this base class will now have all the knowledge of the fixtures and can now be inherited wherever needed instead of using fixtures for each and every testcase. We need not explicitly define the fixture everywhere
@pytest.mark.usefixtures("web_browser")
class Base:
    pass
# pass is a keyword in python that specifies that we are not performing any operation in this file
