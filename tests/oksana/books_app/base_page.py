from selenium.webdriver.remote.webdriver import WebDriver
from .constants import HOST


class BasePage:
    URL = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        return self.driver.get(HOST + self.URL)


class LoginPage(BasePage):
    URL = "/login"
