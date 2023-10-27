import time

from appium import webdriver
import allure
import pytest
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def appium_driver():
    capabilities = {
        'deviceName': 'Pixel 4 API 34',
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': '14.0',
        'appPackage': 'com.google.android.contacts',
        'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity'
    }
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['appium_driver']  # Get the Appium driver instance
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to take screenshot: {str(e)}")
