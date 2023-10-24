import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

'''
This script automates the process of opening the Phone Dialer app, 
bringing up the dial pad, and pressing the numbers 1, 2, 3, and 5 in sequence on an Android device.
'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appPackage': 'com.google.android.dialer',
    'appActivity': 'com.android.dialer.main.impl.MainActivity'
}

appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options()
options.load_capabilities(capabilities)

driver = webdriver.Remote(appium_server_url, options=options, direct_connection=True)
driver.implicitly_wait(5)

# driver.press_keycode()

driver.find_element(by=AppiumBy.ID, value="com.google.android.dialer:id/dialpad_fab").click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/one').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/two').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/three').click()
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/five').click()

time.sleep(2)
driver.quit()
