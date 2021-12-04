from typing import List

from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseElement:

    def __init__(self, driver: WebElement):
        self.driver = driver

    def get_element(self, by_locator) -> WebElement:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_elements(self, by_locator) -> List[WebElement]:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return self.driver.find_elements(*by_locator)

    def get_element_text(self, by_locator):
        return self.get_element(by_locator).text

    def do_click(self, by_locator):
        self.get_element(by_locator).click()

    def do_send_keys(self, by_locator, text):
        self.get_element(by_locator).send_keys(text)

    def is_visible(self, by_locator):
        return bool(self.get_element(by_locator))


class BasePage(BaseElement):
    host = None
    url = None
    title = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        assert self.url
        self.driver.get(self.host + self.url)
        return self

    def get_title(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains(self.title))
        return self.driver.title


class GetItem:

    def __init__(self, by=By.ID, value=None):
        self.by = by
        self.value = value

    def __get__(self, instance: BaseElement, owner) -> WebElement:
        return instance.get_element((self.by, self.value))
