from tests.osokolov.book_store.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

from tests.osokolov.book_store.login_page_elements import LoginPageElements


class LoginPage(BasePage):
    HOST = 'https://demoqa.com'
    URL = '/login'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.login_page = LoginPageElements()

    def sign_in(self, username, password):
        self.element(self.login_page.username_field).send_keys(username)
        self.element(self.login_page.password_field).send_keys(password)
        self.element(self.login_page.login_button).click()

    def verify_login_page(self):
        assert self.element(self.login_page.login_page_header).text == 'Login'
