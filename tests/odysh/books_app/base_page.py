from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from .constants import HOST


class BasePage:
    URL = ""
    HEADER = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def navigate_to_page(self):
        self.driver.get(HOST + self.URL)
        return self.on_load

    @property
    def header(self):
        return self.find_element(By.CSS_SELECTOR, ".main-header").text

    @property
    def wait(self) -> Wait:
        return Wait(self.driver, 5)

    @property
    def on_load(self):
        self.wait.until(EC.url_contains(self.URL))
        return self
