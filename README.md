# python-appium

1. Install Appium Server: `npm i -g appium`
2. Install Appium-Python-Client: `pip3 install Appium-Python-Client`
3. Launch Appium server: `appium` (Run on http://127.0.0.1:4723/)
4. Install Selenium: `pip3 install selenium` 


#### Locate Elements
- Open chrome://inspect/#devices on Chrome browser of your local machine

#### kill process`
- `kill $(lsof -t -i:4723)`

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

#### Note
- The `uiautomatorviewer` tool typically requires Java 8

#### Reference
- python-client doc: https://appium.github.io/python-client-sphinx/
- selenium doc: https://www.selenium.dev/documentation/