from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:
    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        scroll_command = "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new " \
                         "UiSelector().textContains(\"+text+\").instance(0))"
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command).click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(howManySwipes):
            driver.swipe(590, 1740, 590, 670, 1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes):
            driver.swipe(590, 670, 590, 1740, 1000)
