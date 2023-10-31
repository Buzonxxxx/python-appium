from Pages.HomeScreen import HomeScreen
from BaseTest import BaseTest


class Test_AddContacts(BaseTest):
    def test_contacts(self):
        home = HomeScreen(self.driver)
        home.enterAddContact().addContacts('Harry', '0987654')
