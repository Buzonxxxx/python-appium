import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

'''
The script is intended to demonstrate how to automate browser interactions on an Android device 
using Appium and entering text in Google search text field.
'''

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'browserName': 'Chrome'
}
appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

driver.get('http://google.com')
print(driver.title)
driver.find_element(By.XPATH, "//*[@id='XSqSsc']").send_keys("Hello Appium!!!")
time.sleep(2)
driver.quit()


