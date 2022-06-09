from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    HOST = None
    URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    def open(self):
        return self.driver.get(f'{self.HOST}{self.URL}')

    def element(self, by: Tuple[By, str]):
        return self.driver.find_element(*by)

    def collection(self, by: Tuple[By, str]):
        return self.driver.find_elements(*by)

    def refresh_page(self):
        self.driver.refresh()
