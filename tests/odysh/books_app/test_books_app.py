from selenium.webdriver.remote.webdriver import WebDriver

from tests.odysh.books_app.constants import USER

from tests.odysh.books_app.pages import BooksPage, LoginPage, ProfilePage


def test_login(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.navigate_to_page()
    login_page.login()
    assert login_page.header == ProfilePage.HEADER

def test_user_name(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_page()
    login_page.login()
    assert ProfilePage(driver).logged_in_user_name() == USER

def test_search_book(driver):
    books_page = BooksPage(driver)
    books_page.navigate_to_page()
    assert books_page.search_book() == 'Git Pocket Guide'

def test_qweqwe(driver):
    books_page = BooksPage(driver)
    books_page.navigate_to_page()
