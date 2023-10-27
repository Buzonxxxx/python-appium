from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_contacts(appium_driver):
    driver = appium_driver
    driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
    # Waiting until the create button comes up
    try:
        create_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Create contact')))
        create_button.click()
    except TimeoutException as ex:
        print("Exception has been thrown. " + str(ex))

    # Use uiautomator uiselector
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='text("First name")').send_keys("Harry")

    # Use customize XPATH
    driver.hide_keyboard()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("098765")
    driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@text, "Save")]').click()
