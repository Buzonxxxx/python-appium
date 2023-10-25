
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from testcases.android.actions_util import ActionsUtil

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
time.sleep(1)


# Note: Enable Pointer Location in Developer Options

# Drag and Drop
# names = driver.find_elements(AppiumBy.ID, 'com.google.android.contacts:id/cliv_name_textview')
# ActionsUtil.dragAndDrop(names[0], names[5], driver)

# Long press
# anney = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Anney")')
# ActionsUtil.longPress(anney, driver)

# Scroll from bottom to top
ActionsUtil.swipeUp(2, driver)

# Scroll into view
# ActionsUtil.scrollToTextByAndroidUIAutomator('Lucas', driver)

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Anney")').click()

time.sleep(2)
driver.quit()
