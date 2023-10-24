import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

'''
This script demonstrates how to start the Appium server programmatically, 
interact with web elements (specifically dropdowns) in a mobile browser using Appium and Selenium, 
and how to clean up by stopping the Appium server programmatically.
'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'browserName': 'Chrome'
}

# Start Appium Server programmatically
appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)

appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options()
options.load_capabilities(capabilities)

driver = webdriver.Remote(appium_server_url, options=options, direct_connection=True)
driver.implicitly_wait(5)

driver.get('http://wikipedia.com')
print(driver.title)
dropdown = driver.find_element(By.CSS_SELECTOR, "#searchLanguage")
select = Select(dropdown)
select.select_by_value("hi")

options = driver.find_elements(By.TAG_NAME, 'option')

print(len(options))

for option in options:
    print(f'Text is: {option.text} Lang is: {option.get_attribute("Lang")}')

time.sleep(2)
driver.quit()
appium_service.stop()


