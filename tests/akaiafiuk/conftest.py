import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver

from python_at_2021.tests.akaiafiuk.book_store_ui.books_test import LoginPage
from python_at_2021.tests.akaiafiuk.constants import LOGIN, PASSWORD


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


@pytest.fixture()
def prepared_user(session) -> WebDriver:
    session.delete_all_cookies()
    session.refresh()
    login_page = LoginPage(session)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    yield session
    session.delete_all_cookies()
    session.refresh()
