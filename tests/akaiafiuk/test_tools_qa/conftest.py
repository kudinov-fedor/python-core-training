from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
import pytest


@pytest.fixture
def session() -> WebDriver:
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
