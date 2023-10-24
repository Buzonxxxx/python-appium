import time
from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options

'''
Install the apk
'''

apk_path = str(Path.cwd() / "apks/Amazon_shopping.apk")

capabilities = {
    'deviceName': 'Pixel 4 API 34',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appium:app': apk_path
}

# capabilities = {
#     "deviceName": "Pixel 3",
#     "platformName": "Android",
#     "automationName": "UiAutomator2",
#     "platformVersion": "13",
#     'appium:app': apk_path
# }

appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options()
options.load_capabilities(capabilities)

driver = webdriver.Remote(appium_server_url, options=options, direct_connection=True)
driver.implicitly_wait(5)

time.sleep(2)
driver.quit()


