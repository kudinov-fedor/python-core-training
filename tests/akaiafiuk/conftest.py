import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture()
def test_list():
    return [1, 2, 3]


@pytest.fixture(scope='session')
def session() -> WebDriver:
    driver = Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
