from Pages.BasePage import BasePage


class EditContactsScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def addContacts(self, name, number):
        self.send_keys("first_name_editText_TEXT", name)
        self.send_keys("phone_editText_XPATH", number)
        self.click("save_button_XPATH")
