from selenium.webdriver import Chrome
import pytest


@pytest.fixture
def akaiafiuk_session():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
