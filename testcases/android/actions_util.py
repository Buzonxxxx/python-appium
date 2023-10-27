from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


class ActionsUtil:
    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        scroll_command = f"new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
                         f").textContains(\"{text}\").instance(0))"
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command).click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(howManySwipes):
            driver.swipe(590, 1740, 590, 670, 1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes):
            driver.swipe(590, 670, 590, 1740, 1000)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        for i in range(1, howManySwipes):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes):
            driver.swipe(200, 600, 900, 600, 1000)

    @staticmethod
    def longPress(element, driver):
        actions = TouchAction(driver)
        actions.long_press(element).perform()

    @staticmethod
    def dragAndDrop(start, end, driver):
        actions = TouchAction(driver)
        actions.press(start).wait(3000).move_to(end).perform().release()
