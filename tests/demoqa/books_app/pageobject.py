from .constants import USER, PASSWORD

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    host = "https://demoqa.com"
    url = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.host + self.url)
        return self

    def find_elenent(self, by, value):
        return self.driver.find_element(by, value)

    def find_elenents(self, by, value):
        return self.driver.find_elements(by, value)

    @property
    def header(self):
        return self.find_elenent(By.CSS_SELECTOR, ".main-header").text

    @property
    def on_load(self):
        self.wait.until(EC.url_contains(self.url))
        return self

    @property
    def wait(self) -> Wait:
        return Wait(self.driver, 10)


class LoginPage(BasePage):
    url = "/login"

    def login(self, user: str = None, password: str = None):
        userName = self.find_elenent(By.CSS_SELECTOR, "#userName")
        userName.clear()
        userName.send_keys(user or USER)

        passwordField = self.find_elenent(By.CSS_SELECTOR, "#password")
        passwordField.clear()
        passwordField.send_keys(password or PASSWORD)

        self.find_elenent(By.CSS_SELECTOR, "button#login").click()

        self.wait.until(EC.url_changes(self.url))

        return ProfilePage(self.driver)

    def logout(self):
        ...

    def user_loged_in(self) -> bool:
        ...


class BooksPage(BasePage):
    url = "/books"


class ProfilePage(BasePage):
    url = "/profile"
