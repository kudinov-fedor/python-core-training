from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from python_at_2021.tests.akaiafiuk.book_store_ui.pages.page import Page


class LoginPage(Page):
    url = '/login'

    USERNAME_INPUT = By.CSS_SELECTOR, '#userName'
    PASSWORD_INPUT = By.CSS_SELECTOR, '#password'

    LOGIN_BTN = By.CSS_SELECTOR, 'button#login'
    NEW_USER_BTN = By.CSS_SELECTOR, 'button#newUser'

    def login(self, username: str, password: str) -> None:
        """
        Login using given credentials
        :param username: string
        :param password: string
        :return: None
        """
        self.element(LoginPage.USERNAME_INPUT).send_keys(username)
        self.element(LoginPage.PASSWORD_INPUT).send_keys(password)
        self.element(LoginPage.LOGIN_BTN).click()
        Wait(self.session, 5).until(EC.url_changes(self.host + self.url))
