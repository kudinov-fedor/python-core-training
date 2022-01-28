from tests.odysh.books_app.constants import USER, PASSWORD
from tests.odysh.books_app.locators import LoginPageLocators
from .base_page import BasePage
from .profile_page import ProfilePage


class LoginPage(BasePage):
    URL = "/login"
    HEADER = "Login"

    def login(self):
        user_name = self.find_element(*LoginPageLocators.user_name_field)
        user_name.send_keys(USER)
        password_field = self.find_element(*LoginPageLocators.pwd_name_field)
        password_field.send_keys(PASSWORD)
        self.find_element(*LoginPageLocators.login_btn).click()
        return ProfilePage(self.driver).on_load
