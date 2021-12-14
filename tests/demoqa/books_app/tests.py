import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_helpers.session import create_session
from .pageobject import BasePage, LoginPage, BooksPage, ProfilePage


@pytest.fixture(scope="session")
def session() -> WebDriver:
    session = create_session()
    yield session
    session.quit()


def test_login(session: WebDriver):
    login_page = LoginPage(session)
    profile_page = ProfilePage(session)

    login_page.open().login()
    assert profile_page.on_load.header == "Profile"
