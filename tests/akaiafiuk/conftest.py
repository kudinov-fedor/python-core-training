import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from python_at_2021.tests.akaiafiuk.constants import HOST


@pytest.fixture()
def test_list():
    return [1, 2, 3]


@pytest.fixture(scope='session')
def session() -> WebDriver:
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def bookstore_session(session) -> WebDriver:
    session.get(HOST + '/books')
    return session
