import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_helpers.session import create_session
from .pageobject import BasePage, LoginPage, BooksPage, ProfilePage, BookPage  # noqa: F401


@pytest.fixture(scope="session")
def session() -> WebDriver:
    session = create_session()
    session.implicitly_wait(0.5)
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def remove_books(session):
    LoginPage(session).open().login()
    ProfilePage(session).remove_books().logout()


@pytest.fixture(autouse=True)
def clear_cache(session):
    yield
    session.delete_all_cookies()
    session.refresh()


def test_login_logout(session: WebDriver):
    login_page = LoginPage(session)
    profile_page = ProfilePage(session)

    login_page.open().login()
    assert profile_page.on_load.header == ProfilePage.HEADER
    assert not profile_page.has_books()
    assert profile_page.logout().on_load.header == LoginPage.HEADER


def test_search(session):
    books_page = BooksPage(session).open()
    assert len(books_page.get_books()) == 8
    assert len(books_page.search("ECMA").get_books()) == 1


def test_search_empty(session):
    books_page = BooksPage(session).open().on_load
    assert len(books_page.get_books()) == 8
    assert len(books_page.search("Some wierd title").get_books()) == 0


def test_add_books(session):
    LoginPage(session).open().login()
    BooksPage(session).open().go_to_book(1).add_book()
    assert len(ProfilePage(session).open().get_books()) == 1
