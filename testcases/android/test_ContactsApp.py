import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

'''
This script essentially automates the process of adding a new contact named "Harry" 
with the phone number "098765" to the Contacts app on an Android device.
'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appPackage': 'com.google.android.contacts',
    'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity'
}

appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options()
options.load_capabilities(capabilities)

driver = webdriver.Remote(appium_server_url, options=options, direct_connection=True)
driver.implicitly_wait(5)

driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
time.sleep(1)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create contact').click()

# Use customize XPATH
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]').send_keys("Harry")
driver.hide_keyboard()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("098765")
driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@text, "Save")]').click()


time.sleep(2)
driver.quit()


