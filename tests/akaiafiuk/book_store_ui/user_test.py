import pytest
from python_at_2021.tests.akaiafiuk.constants import LOGIN
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.books_page import BooksPage


@pytest.mark.user
def test_login(prepared_user):
    """
    Login using existing user
    """
    books = BooksPage(prepared_user).open()
    assert prepared_user.get_cookie('token')
    assert books.get_displayed_username() == LOGIN


@pytest.mark.user
def test_remove_cookies(prepared_user):
    """
    Verify that user is not authorized after removing cookies
    """
    prepared_user.delete_all_cookies()
    books = BooksPage(prepared_user).open()
    assert not books.user_is_logged_in()
