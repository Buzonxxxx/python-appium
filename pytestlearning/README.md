

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
- 

