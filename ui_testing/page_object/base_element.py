from selenium.webdriver.remote.webdriver import WebDriver, WebElement


class BaseElement:

    def __init__(self, driver: WebDriver, locator: tuple):
        self.driver = driver
        self.locator = locator

    def _find_element(self) -> WebElement:
        return self.driver.find_element(*self.locator)

    def click(self):
        self._find_element().click()

    def send_keys(self, value):
        self._find_element().send_keys(value)
