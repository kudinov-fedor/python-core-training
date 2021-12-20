from time import sleep
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from tests.demoqa.books_app.constants import USER, PASSWORD


HOST = "https://demoqa.com"
BOOKS_URL = HOST + "/books"
PROFILE_URL = HOST + "/profile"


class BooksPage:

    HOST = "https://demoqa.com"
    URL = HOST + "/books"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_books(self) -> List[WebElement]:
        books = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'books-wrapper')]"
                                                    "//img/ancestor::div[contains(@class, 'rt-tr-group')]")
        sleep(2)
        return books

    def get_books_count(self) -> int:
        books = self.get_books()
        return len(books)


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, login: str = None, password: str = None):
        # login
        self.driver.find_element(By.ID, "login").click()  # go to login page
        self.driver.find_element(By.ID, "userName").send_keys(login or USER)
        self.driver.find_element(By.ID, "password").send_keys(password or PASSWORD)
        self.driver.find_element(By.ID, "login").click()  # go to bookstore page
        sleep(2)


def test_books(session: WebDriver):
    # view books
    # register - SKIP
    # login
    # view books
    # add 2 books
    # view own books
    # remove own book
    # remove all own books
    # logout
    # login - SKIP
    # remove profile - SKIP

    # view books
    session.get(BOOKS_URL)

    # get books_count
    books_page = BooksPage(session)

    assert books_page.get_books_count() == 8

    session.find_element(By.ID, "searchBox").send_keys("JavaScript ")
    assert books_page.get_books_count() == 2

    # register - SKIP

    # login
    LoginPage(session).login(login=USER, password=PASSWORD)

    # view books
    assert books_page.get_books_count() == 8

    session.find_element(By.ID, "searchBox").send_keys("JavaScript ")
    assert books_page.get_books_count() == 2

    # add book
    books = books_page.get_books()
    books[0].find_element(By.TAG_NAME, "a").click()  # go to item page
    sleep(5)
    session.find_element(By.CSS_SELECTOR, ".text-right #addNewRecordButton").click()
    sleep(2)
    alert = session.switch_to.alert
    assert alert.text == "Book added to your collection."
    alert.accept()
    session.find_element(By.CSS_SELECTOR, ".text-left #addNewRecordButton").click()  # back to books

    # add 2 book
    books = session.find_elements(By.XPATH, "//div[contains(@class, 'books-wrapper')]"
                                            "//img/ancestor::div[contains(@class, 'rt-tr-group')]")
    sleep(5)
    books[2].find_element(By.TAG_NAME, "a").click()  # go to item page
    sleep(5)
    session.find_element(By.CSS_SELECTOR, ".text-right #addNewRecordButton").click()
    sleep(2)
    alert = session.switch_to.alert
    assert alert.text == "Book added to your collection."
    alert.accept()

    # view own books
    session.get(PROFILE_URL)
    sleep(2)
    books = session.find_elements(By.XPATH, "//div[contains(@class, 'profile-wrapper')]"
                                            "//img/ancestor::div[contains(@class, 'rt-tr-group')]")
    assert len(books) == 2

    # remove own book
    books[0].find_element(By.ID, "delete-record-undefined").click()
    sleep(2)
    modal = session.find_element(By.CSS_SELECTOR, ".modal-content")
    modal.find_element(By.ID, "closeSmallModal-ok").click()  # Book deleted.
    sleep(2)
    session.switch_to.alert.accept()

    books = session.find_elements(By.XPATH, "//div[contains(@class, 'profile-wrapper')]"
                                            "//img/ancestor::div[contains(@class, 'rt-tr-group')]")
    assert len(books) == 1

    # remove own books
    session.find_element(By.CSS_SELECTOR, ".buttonWrap .text-right #submit").click()
    sleep(2)
    modal = session.find_element(By.CSS_SELECTOR, ".modal-content")
    modal.find_element(By.ID, "closeSmallModal-ok").click()
    sleep(2)
    alert = session.switch_to.alert
    assert alert.text == "All Books deleted."
    alert.accept()

    # logout
    session.find_element(By.ID, "submit").click()
    sleep(5)

    # login - SKIP
    # remove profile - SKIP
