import time
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as AC

from automationpractice.constants import TIMEOUT


class BaseElement:

    def __init__(self, driver: WebElement):
        self.driver = driver

    @property
    def parent(self):
        return self.driver._parent

    @property
    def ac(self) -> AC:
        return AC(self.parent)

    def get_element(self, by_locator, from_parent=False) -> WebElement:
        time.sleep(TIMEOUT)
        driver = self.parent if from_parent else self.driver
        # return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_locator))
        return driver.find_element(*by_locator)

    def get_elements(self, by_locator, from_parent=False) -> List[WebElement]:
        time.sleep(TIMEOUT)
        driver = self.parent if from_parent else self.driver
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by_locator))
        return driver.find_elements(*by_locator)

    def get_element_text(self, by_locator):
        return self.get_element(by_locator).text

    def do_click(self, by_locator):
        self.get_element(by_locator).click()

    def do_hover(self, by_locator=None):
        el = self.get_element(by_locator) if by_locator else self.driver
        AC(self.parent).move_to_element(el).perform()

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

    @property
    def parent(self):
        return self.driver

    def open_page(self):
        assert self.url
        self.driver.get(self.host + self.url)
        return self

    def get_title(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains(self.title))
        return self.driver.title


class GetItem:

    def __init__(self, by=By.ID, value=None, *, factory=None, from_parent=False):
        """
        Lazy initialization of WebElement for BasePage, BaseElement
        :param by: locator
        :param value: locator
        :param factory: wrapper for selenium.webdriver.remote.webelement.WebElement
        :param from_parent: find WebElement from Webdriver and not from WebElement
        """
        self.by = by
        self.value = value
        self.factory = factory or (lambda i: i)
        self.from_parent = from_parent

    def __get__(self, instance: BaseElement, owner) -> WebElement:
        element = instance.get_element((self.by, self.value), from_parent=self.from_parent)
        return self.factory(element)


class GetItems(GetItem):

    def __get__(self, instance: BaseElement, owner) -> List[WebElement]:
        elements = instance.get_elements((self.by, self.value), from_parent=self.from_parent)
        return [self.factory(element) for element in elements]
