
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from testcases.android.scroll_util import ScrollUtil

'''

'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appPackage': 'com.google.android.contacts',
    'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity'
}

driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))

driver.find_element(AppiumBy.ID, 'android:id/button2').click()

# Scroll from bottom to top (enable Pointer Location in Developer Options)
ScrollUtil.swipeUp(2, driver)

# Scroll into view
# ScrollUtil.scrollToTextByAndroidUIAutomator('Lucas', driver)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Lucas")').click()

time.sleep(2)
driver.quit()
