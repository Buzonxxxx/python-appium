

 `pytest test_marker_example.py -s -v -k login`
 `pytest test_marker_example.py -s -v -k "not login"` 
 
#### Register marker
- add `pytest.ini`
- `pytest test_marker_example.py -s -v -m "not functional"`

#### Soft assertion
`pip3 install pytest-soft-assertions`
`pytest test_validate_titles.py -s -v --soft-asserts`

#### HTML Report
` pip3 install pytest-html`
` pytest test_validate_titles.py --html=testreports.html`

#### Allure Report
- Doc: https://allurereport.org/docs/gettingstarted/installation/
- `brew install allure`
- `pip3 install allure-pytest`
-  Create `allurereports` folder
- `pytest test_validate_titles.py --alluredir="./allurereports"` 
- `allure serve ./allurereports`
- Save screenshot `allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)`

#### Get Screenshot when test failure
1. Add `conftest.py`
   - The `conftest.py` file serves as a means of providing fixtures for an entire directory.
2. See sample `test_appium_integration.py`
3. Run `pytest test_validate_titles.py --alluredir="./allurereports"` 
4. Run `allure serve ./allurereports`

#### Parallel Execution
1. Install `pytest-xdist`
2. Add `addopts = -n2` in `pytest.ini`
3. Update `conftest.yp`
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