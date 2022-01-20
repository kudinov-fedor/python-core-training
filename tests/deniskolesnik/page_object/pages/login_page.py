from selenium.webdriver.common.by import By

from page_object import env_variable
from page_object.pages.base_page import BasePage
from page_object.pages.profile_page import Profile


class LoginPage(BasePage):

    URL = '/login'
    login_wrapper = '.login-wrapper'
    username_field = '#userName'
    password_field = '#password'
    login_button = '#login'
    new_user_button = '#newUser'

    def login_form(self):
        return self.find_element(By.CSS_SELECTOR, self.login_wrapper)

    def login(self):
        username = self.find_element(By.CSS_SELECTOR, self.username_field)
        password = self.find_element(By.CSS_SELECTOR, self.password_field)

        username.clear()
        username.send_keys(env_variable.USERNAME)

        password.clear()
        password.send_keys(env_variable.PASSWORD)

        self.find_element(By.CSS_SELECTOR, self.login_button).click()

        Profile(self.driver).on_load()

        return self.driver.current_url
