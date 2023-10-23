import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'browserName': 'Chrome'
}
appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options()
options.load_capabilities(capabilities)

driver = webdriver.Remote(appium_server_url, options=options, direct_connection=True)

driver.get('http://google.com')
print(driver.title)
# driver.find_element(by=AppiumBy.XPATH, value="//*[@name='q']").send_keys("Hello Appium!!!")
driver.find_element(by=AppiumBy.XPATH, value="//*[@id='XSqSsc']").send_keys("Hello Appium!!!")
time.sleep(2)
driver.quit()


