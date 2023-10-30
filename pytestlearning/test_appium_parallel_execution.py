import pytest
from selenium.webdriver.common.by import By


def test_dologin(appium_driver):
    driver = appium_driver
    driver.get('http://google.com')
    driver.find_element(By.XPATH, "//*[@id='XSqSsc']").send_keys("Hello Appium!!!")

