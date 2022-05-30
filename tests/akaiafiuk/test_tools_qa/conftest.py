from selenium.webdriver import Chrome
import pytest


@pytest.fixture
def session():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
