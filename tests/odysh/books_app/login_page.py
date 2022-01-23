from selenium.webdriver.common.by import By

from .base_page import BasePage
from .profile_page import ProfilePage
from .constants import *


class LoginPage(BasePage):
    URL = "/login"
    HEADER = "Login"

    def login(self):
        user_name = self.find_element(By.ID, user_name_field)
        user_name.send_keys(USER)
        password_field = self.find_element(By.ID, pwd_name_field)
        password_field.send_keys(PASSWORD)
        self.find_element(By.ID, login_btn).click()
        return ProfilePage(self.driver).on_load
