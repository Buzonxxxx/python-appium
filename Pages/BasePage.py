from appium.webdriver.common.appiumby import AppiumBy

from utilities.configReader import readConfig


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=AppiumBy.XPATH, value=readConfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(by=AppiumBy.ID, value=readConfig("locators", locator)).click()
        elif str(locator).endswith("_TEXT"):
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=readConfig("locators", locator)).click()

    def send_keys(self, locator, content):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(by=AppiumBy.XPATH, value=readConfig("locators", locator))\
                .send_keys(content)
            self.driver.hide_keyboard()
        if str(locator).endswith("_TEXT"):
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=readConfig("locators", locator))\
                .send_keys(content)
            self.driver.hide_keyboard()

