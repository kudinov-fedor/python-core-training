from selenium.webdriver.common.by import By

from page_object import env_variable
from page_object.pages.base_page import BasePage
from page_object.pages.profile_page import Profile


class LoginPage(BasePage):

    URL = '/login'
    LOGIN_WRAPPER = By.CSS_SELECTOR, '.login-wrapper'
    USERNAME_FIELD = '#userName'
    PASSWORD_FIELD = '#password'
    LOGIN_BUTTON = '#login'
    NEW_USER_BUTTON = '#newUser'

    def login_form(self):
        return self.find_element(*self.LOGIN_WRAPPER)

    def login(self):
        username = self.find_element(By.CSS_SELECTOR, self.USERNAME_FIELD)
        password = self.find_element(By.CSS_SELECTOR, self.PASSWORD_FIELD)

        username.clear()
        username.send_keys(env_variable.USERNAME)

        password.clear()
        password.send_keys(env_variable.PASSWORD)

        self.find_element(By.CSS_SELECTOR, self.LOGIN_BUTTON).click()

        Profile(self.driver).on_load()

        return self.driver.current_url
