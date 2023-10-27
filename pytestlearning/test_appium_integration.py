from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_contacts(appium_driver):
    appium_driver.find_element(by=AppiumBy.ID, value='android:id/button2').click()
    # Waiting until the create button comes up
    try:
        create_button = WebDriverWait(appium_driver, 2).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Create contact')))
        create_button.click()
    except TimeoutException as ex:
        print("Exception has been thrown. " + str(ex))

    # Use uiautomator uiselector
    appium_driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='text("First name")').send_keys("Harry")

    # Use customize XPATH
    appium_driver.hide_keyboard()
    appium_driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("098765")
    appium_driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@text, "Saveasd")]').click()
