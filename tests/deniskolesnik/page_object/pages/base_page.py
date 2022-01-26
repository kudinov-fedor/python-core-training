from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from page_object import env_variable


class BasePage:
    LOGOUT_BUTTON = '//button[text()="Log out"]'
    BOOK_STORE = ''

    URL = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def on_load(self):
        self.wait.until(EC.url_contains(self.URL))
        return self

    @property
    def wait(self) -> Wait:
        return Wait(self.driver, 10)

    def open(self):
        self.driver.get(env_variable.HOST + self.URL)
        return self.on_load()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def logout(self):
        self.find_element(By.XPATH, self.LOGOUT_BUTTON).click()
        self.wait.until(EC.url_contains('/login'))
        return self
