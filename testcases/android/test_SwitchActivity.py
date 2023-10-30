
import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

''' 
'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appPackage': 'com.android.chrome',
    # 'noReset': True,
    'appActivity': 'org.chromium.chrome.browser.ChromeTabbedActivity'
}
driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))
driver.implicitly_wait(10)

time.sleep(2)
os.system("adb -s emulator-5556 shell am start -n com.google.android.contacts/com.google.android.apps.contacts.activities.PeopleActivity")
driver.find_element()
time.sleep(2)
driver.quit()



