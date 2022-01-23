from selenium.webdriver.common.by import By

from .books_page import BooksPage
from .constants import user_name_value


class ProfilePage(BooksPage):
    URL = "/profile"
    HEADER = "Profile"

    def logged_in_user_name(self):
        return self.find_element(By.ID, user_name_value).text
