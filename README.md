# python-appium

## Installation
1. Install Appium Server: `npm i -g appium`
2. Install Appium-Python-Client: `pip3 install Appium-Python-Client`
3. Launch Appium server: `appium` (Run on http://127.0.0.1:4723/)
4. Install Selenium: `pip3 install selenium` 

## Mobile Web
#### Locate Mobile Web UI Elements
- Open chrome://inspect/#devices on Chrome browser of your local machine

## Native Apps
#### Get app package and activity
```bash
adb -s <device_serial_number> shell 
dumpsys window windows | grep -E 'mTopActivityComponent'
```
the result should look like this
```bash
mTopActivityComponent=com.google.android.dialer/com.android.dialer.main.impl.MainActivity
```
the package is : `com.google.android.dialer`

the activity is: `com.android.dialer.main.impl.MainActivity`

#### kill process
- `kill $(lsof -t -i:4723)`

#### Backup apks
- Install es file explorator from Play Store
- Long press the app and select backup apk
- Use Android Studio's Device Manager to download the backup apks
- Path: `/sdcard/[Your apk]`
#### Note
- The `uiautomatorviewer` tool typically requires Java 8


#### Reference
- python-client doc: https://appium.github.io/python-client-sphinx/
- selenium doc: https://www.selenium.dev/documentation/
- uiautomator UiSelector: https://developer.android.com/reference/androidx/test/uiautomator/UiSelector

#### Snippets
```text
[Mobile Web]
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

Find Element
driver.find_element(By.CLASS_NAME, "login_logo")
driver.find_element(By.ID, 'user-name')
driver.find_element(By.CSS_SELECTOR, "#searchLanguage")
driver.find_elements(By.TAG_NAME, 'option')
driver.find_element(By.XPATH, "//*[@id='XSqSsc']")

Action
[element].clear()
[element].send_keys('secret_sauce')
[element].click()
[element].get_attribute("clickable")
select = Select(dropdown)
select.select_by_value("hi")

Assertion
assert 'Swag Labs' in driver.page_source
assert 'Products' in title.text

[App]
driver.hide_keyboard()
driver.press_keycode()

Find Element
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]')
driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/one')
driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='text("First name")')

Wait Method
// explicit wait
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 2).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Create contact')))

// implicit wait
driver.implicitly_wait(5)


```


