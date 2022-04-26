import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from APK.Apkcode import APK


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    app_obj = APK()
    app_path = app_obj.CX_apk("1.31.0")
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['appPackage'] = 'live.citymall.customer.prod'
    desired_caps['appActivity'] = 'live.citymall.customer.MainActivity'
    desired_caps['noReset'] = False
    desired_caps['autoGrantPermissions'] = True
    desired_caps['app'] = app_path

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    request.cls.driver = driver
    

    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
