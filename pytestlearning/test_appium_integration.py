import time

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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


def teardown_module(module):
    time.sleep(2)
    driver.quit()


def test_contacts():
    driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
    # Waiting until the create button comes up
    try:
        create_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Create contact')))
        create_button.click()
    except TimeoutException as ex:
        print("Exception has been thrown. " + str(ex))

    # Use uiautomator uiselector
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='text("First name")').send_keys("Harry")

    # Use customize XPATH
    driver.hide_keyboard()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("098765")
    driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@text, "Save")]').click()
    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

