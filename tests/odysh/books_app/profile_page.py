from .books_page import BooksPage
from .locators import ProfilePageLocators


class ProfilePage(BooksPage):
    URL = "/profile"
    HEADER = "Profile"

    def logged_in_user_name(self):
        return self.find_element(*ProfilePageLocators.user_name_value).text
