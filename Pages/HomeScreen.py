import time

from Pages.BasePage import BasePage
from Pages.EditContactsScreen import EditContactsScreen


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enterAddContact(self):
        time.sleep(1)
        self.click("skip_button_ID")
        self.click("create_button_ACCESSIBILITYID")
        return EditContactsScreen(self.driver)