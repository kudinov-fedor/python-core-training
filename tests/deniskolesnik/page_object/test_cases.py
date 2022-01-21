from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from page_object import env_variable
from page_object.pages import BasePage, LoginPage, Profile, BookPage, BookStore


def test_login(driver_init):
    LoginPage(driver_init).open().login()
    driver_init.find_element(By.XPATH, BasePage(driver_init).LOGOUT_BUTTON)

def test_logout(driver_init):
    test_login(driver_init)
    BasePage(driver_init).logout()

    try:
        LoginPage(driver_init).login_form()
    except NoSuchElementException:
        return AssertionError('User is not logged out')


def test_search_and_add_book_to_collecton(driver_init):
    test_delete_all_books(driver_init)

    open_book = BookStore(driver_init).open().search_book_and_open(env_variable.BOOK_NAME)
    assert open_book in driver_init.current_url

    add_book = BookPage(driver_init).add_book_to_collection()
    assert add_book == 'Book added to your collection.'


def test_delete_all_books(driver_init):
    test_login(driver_init)
    Profile(driver_init).open().check_if_books_added()
