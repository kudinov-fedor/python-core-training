from typing import Tuple, List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement


class BaseElement(WebElement):
    def __init__(self, session: WebElement):
        self.session = session

    def parent(self) -> WebDriver:
        return self.session.parent

    def element(self, by: Tuple[By, str]) -> WebElement:
        return self.session.find_element(*by)

    def elements(self, by: Tuple[By, str]) -> List[WebElement]:
        return self.session.find_elements(*by)
