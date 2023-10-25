
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

'''
[contexts]
NATIVE_APP
WEBVIEW_chrome

Demonstrates how to use Appium to automate interactions within the Chrome browser on an Android device. 
'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appPackage': 'com.android.chrome',
    'appActivity': 'org.chromium.chrome.browser.ChromeTabbedActivity'
}
driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))
driver.implicitly_wait(10)

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="No thanks"]').click()

driver.get('http://google.com')
contexts = driver.contexts
for context in contexts:
    print(context)

driver.switch_to.context('WEBVIEW_chrome')

driver.find_element(By.XPATH, "//*[@name='q']").send_keys("Hello Appium!!!")


time.sleep(2)
driver.quit()
