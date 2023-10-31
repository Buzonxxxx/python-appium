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
- Allow auto download chromedriver `appium server --allow-insecure chromedriver_autodownload`


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
## Utilities
#### Add log utilities
1. Add `generating_logs.py`
    ```
    def log():
        logging.basicConfig(filename="../logs/logfile.log", format='%(asctime)s: %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.INFO)
    
        logger = logging.getLogger()
    
        return logger
    ```
#### Add Config Reader
1. Add `config.ini`
    ```
   [basic info]
    testsiteurl=http://gmail.com
    browser=chrome
    implicit.wait=10
    explicit.wait=5
   ```
2. Add `reader.py`
    ```pycon
    def readConfig(section, key):
        config = ConfigParser()
        config.read('config.ini')
        return config.get(section, key)
    ```
#### Read and Write Excel(.xlsx) file
1. Install `openpyxl`
2. Read excel
   ```pycon
   import openpyxl

   workbook = openpyxl.load_workbook('Chiuhsien.xlsx')
   sheet = workbook['Quiz']
   total_rows = sheet.max_row
   print(f'total rows are: {total_rows}, and total cols are: {total_cols}')
   total_cols = sheet.max_column
   ```
3. Write excel
   ```pycon
   import openpyxl

   workbook = openpyxl.load_workbook('sample.xlsx')
   sheet = workbook['Quiz']
   
   sheet.cell(row=2, column=3).value = 'age'
   workbook.save('./new.xlsx')
   ```
#### Interact with DB(mysql)
1. Install `mysql-connector-python`
2. Sample
   ```pycon
   import mysql.connector
   
   
   def createDbConnection():
       global mydb
       mydb = mysql.connector.connect(
   
           host="localhsot",
           user="root",
           password="selenium",
           database="pydb"
   
       )
   
   
   def getMysqlQuery(query):
       mycusor = mydb.cursor()
       mycusor.execute(query)
       myresult = mycusor.fetchone()
       return myresult[0]
   ```

## Parallel Execution - Use py-xdist
1. Install `pytest-xdist`
2. Add `addopts = -n2` in `pytest.ini`
3. Update `conftest.py`
    ```pycon
   @pytest.fixture(params=["device1", "device2"], scope="function")
    def appium_driver(request):
    if request.param == "device1":
        capabilities = {
            'deviceName': 'Pixel 4 API 34',
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '14.0',
            'browserName': 'Chrome',
            'udid': 'emulator-5556'
        }
        driver = webdriver.Remote('http://localhost:4724',
                                  options=UiAutomator2Options().load_capabilities(capabilities))
    if request.param == "device2":
        capabilities = {
            'deviceName': 'Pixel 4 API 34-2',
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '14.0',
            'browserName': 'Chrome',
            'udid': 'emulator-5560'
        }
        driver = webdriver.Remote('http://localhost:4725',
                                  options=UiAutomator2Options().load_capabilities(capabilities))

    yield driver
    time.sleep(2)
    driver.quit()
   ```
4. Launch multiple appium servers
5. Run the test

## Run parallel test using Selenium Grid
1. Download Selenium Grid stable version
2. Add `addopts = -n2` in `pytest.ini`
3. Update `conftest.py` (modify port to 4444)
   ```pycon
   @pytest.fixture(params=["device1", "device2"], scope="function")
   def appium_driver(request):
    if request.param == "device1":
        capabilities = {
            'deviceName': 'Pixel 4 API 34',
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '14.0',
            'browserName': 'com.google.android.contacts',
            'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity',
            'udid': 'emulator-5556'
        }
        driver = webdriver.Remote('http://localhost:4444',
                                  options=UiAutomator2Options().load_capabilities(capabilities))
    if request.param == "device2":
        capabilities = {
            'deviceName': 'Pixel 4 API 34-2',
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '14.0',
            'appPackage': 'com.google.android.contacts',
            'appActivity': 'com.google.android.apps.contacts.activities.PeopleActivity',
            'udid': 'emulator-5560'
        }
        driver = webdriver.Remote('http://localhost:4444',
                                  options=UiAutomator2Options().load_capabilities(capabilities))

    yield driver
    time.sleep(2)
    driver.quit()
   ```
4. Create `appium1.yml`
   ```yaml
   # appium1.yml
   server:
   port: 4724
   use-drivers:
      - UiAutomator2
   ```
5. Create `appium2.yml`
   ```yaml
   # appium1.yml
   server:
   port: 4725
   use-drivers:
      - UiAutomator2
   ```
6. Create `node1.toml`
   ```toml
   # node1.toml
   [server]
   port = 5555
   
   [node]
   detect-drivers = false
   
   [relay]
   url = "http://localhost:4724"
   status-endpoint = "/status"
   configs = [
       "1", "{\"platformName\": \"Android\", \"appium:platformVersion\": \"14.0\", \"appium:deviceName\": \"Pixel 4 API 34\", \"appium:automationName\": \"UiAutomator2\"}"
   ]
   ```
7. Create `node2.toml`
   ```toml
   # node2.toml
   [server]
   port = 5565
   
   [node]
   detect-drivers = false
   
   [relay]
   url = "http://localhost:4725"
   status-endpoint = "/status"
   configs = [
       "1", "{\"platformName\": \"Android\", \"appium:platformVersion\": \"14.0\", \"appium:deviceName\": \"Pixel 4 API 34-2\", \"appium:automationName\": \"UiAutomator2\"}"
   ]
   ```
8. Launch all of services
   ```bash
   appium --config appium1.yml
   appium --config appium2.yml
   java -jar /path/to/selenium.jar node --config node1.toml
   java -jar /path/to/selenium.jar node --config node2.toml
   java -jar /path/to/selenium.jar hub 
   ```
9. Check Selenium Grid in `http://localhost:4444/`

Note: If the test did not run, try wipe emulator and launch it again