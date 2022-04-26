import pytest

#this flanky fixture actually rerun all testcases  for number of times mentioned
@pytest.mark.flanky(reruns=5)
@pytest.mark.usefixtures("log_on_failure", "appium_driver")
class BaseTest:
    pass
