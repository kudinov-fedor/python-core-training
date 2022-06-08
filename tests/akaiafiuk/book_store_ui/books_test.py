import pytest
import requests
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from python_at_2021.tests.akaiafiuk.constants import HOST, LOGIN, PASSWORD


class LoginPage:
    USERNAME_INPUT = By.CSS_SELECTOR, '#userName'
    PASSWORD_INPUT = By.CSS_SELECTOR, '#password'

    LOGIN_BTN = By.CSS_SELECTOR, 'button#login'
    NEW_USER_BTN = By.CSS_SELECTOR, 'button#newUser'

    def __init__(self, session: WebDriver):
        self.session = session

    def open(self) -> None:
        """
        Open Login page
        :return: None
        """
        self.session.get(HOST + '/login')

    def login(self, username: str, password: str) -> None:
        """
        Login using given credentials
        :param username: string
        :param password: string
        :return: None
        """
        self.session.find_element(*LoginPage.USERNAME_INPUT).send_keys(username)
        self.session.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.session.find_element(*LoginPage.LOGIN_BTN).click()


class BooksPage:
    PAGE_TITLE = By.CSS_SELECTOR, '.main-header'
    SEARCH_INPUT = By.CSS_SELECTOR, '#searchBox'
    SEARCH_ICON = By.CSS_SELECTOR, '.input-group-text'
    LOGIN_BUTTON = By.CSS_SELECTOR, '#login'

    COLUMN_TITLES = By.XPATH, '//*[@class="rt-resizable-header-content"]'
    TABLE_ROW = By.XPATH, '//*[@class="action-buttons"]/ancestor::*[@role="row"]'
    BOOK_TITLE = By.XPATH, './/a'
    BOOK_AUTHOR = By.XPATH, './div[3]'
    BOOKS_IMAGES = By.XPATH, './/img'
    BOOKS_LINKS = By.XPATH, './/a'
    USER_NAME = By.CSS_SELECTOR, '#userName-value'

    def __init__(self, session: WebDriver):
        self.session = session

    def open(self) -> None:
        """
        Open Books page
        :return: None
        """
        self.session.get(HOST + '/books')

    def get_rows(self) -> list:
        """
        Get all book rows currently displayed
        :return: list of Web Elements
        """
        return self.session.find_elements(*BooksPage.TABLE_ROW)

    def get_columns(self) -> list:
        """
        Get column titles
        :return: list of web elements
        """
        return self.session.find_elements(*BooksPage.COLUMN_TITLES)

    def get_row_by_id(self, row_id: int) -> WebElement:
        """
        Get a specific row from the list of all rows
        :param row_id: id of a row from the list of rows
        :return: Web element that represents a single row
        """
        return self.get_rows()[row_id]

    @staticmethod
    def get_book_title_from_row(row: WebElement) -> str:
        """
        Returns a string with a book title for a specific row
        :param row: row Web element
        :return: string with a book title
        """
        return row.find_element(*BooksPage.BOOK_TITLE).text

    @staticmethod
    def get_book_author_from_row(row: WebElement) -> str:
        """
        Returns a string with a book author for a specific row
        :param row: row Web element
        :return: string with a book author
        """
        return row.find_element(*BooksPage.BOOK_AUTHOR).text

    def do_search(self, search_text: str) -> None:
        """
        Execute search on the page
        :param search_text: Search criteria
        :return: None
        """
        search_input = self.session.find_element(*BooksPage.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_text)
        search_input.send_keys(Keys.ENTER)

    def get_images(self) -> list:
        """
        Get a list with all images from the books table
        :return: list of Web Elements
        """
        rows = self.session.find_elements(*BooksPage.TABLE_ROW)
        images = list(row.find_element(*BooksPage.BOOKS_IMAGES) for row in rows)
        return images

    def get_links(self) -> list:
        """
        Get a list with all links from the books table
        :return: list of Web Elements
        """
        rows = self.session.find_elements(*BooksPage.TABLE_ROW)
        links = list(row.find_element(*BooksPage.BOOKS_LINKS) for row in rows)
        return links

    def click_login(self) -> None:
        self.session.find_element(*BooksPage.LOGIN_BUTTON).click()

    def get_displayed_username(self) -> str:
        return self.session.find_element(*BooksPage.USER_NAME).text


@pytest.mark.books
def test_locators(session):
    """
    Verify that locators are correct and it is possible to test a separate table row
    """
    books = BooksPage(session)
    books.open()
    row = books.get_row_by_id(0)
    assert books.get_book_title_from_row(row) == 'Git Pocket Guide'
    assert 'Richard E.' in books.get_book_author_from_row(row)


@pytest.mark.books
def test_search(session):
    """
    Test search using exact match
    """
    books = BooksPage(session)
    books.open()
    row = books.get_row_by_id(0)
    title = books.get_book_title_from_row(row)
    books.do_search(title)
    assert len(books.get_rows()) == 1


@pytest.mark.books
def test_column_names(session):
    """
    Test that column names are correct
    """
    expected_titles = ('Image', 'Title', 'Author', 'Publisher')
    books = BooksPage(session)
    books.open()
    columns = books.get_columns()
    assert len(columns) == len(expected_titles)
    assert all(text.text in expected_titles for text in columns)


@pytest.mark.books
def test_books_images(session):
    """
    Test that a valid image is displayed for each book
    """
    books = BooksPage(session)
    books.open()
    for i in books.get_images():
        link = i.get_attribute('src')
        r = requests.head(link)
        assert r.headers['Content-Type'] == 'image/jpeg'


@pytest.mark.books
def test_books_links(session):
    """
    Test that bok links are not broken
    """
    books = BooksPage(session)
    books.open()
    for i in books.get_links():
        link = i.get_attribute('href')
        r = requests.head(link)
        assert 200 <= r.status_code < 400
        r.raise_for_status()


@pytest.mark.user
def test_login(session):
    """
    Login using existing user
    """
    session.delete_cookie('token')
    books = BooksPage(session)
    books.open()
    books.click_login()
    login_page = LoginPage(session)
    login_page.login(LOGIN, PASSWORD)
    assert books.get_displayed_username() == LOGIN
    assert session.get_cookie('token')


@pytest.mark.user
def test_remove_cookies(session):
    """
    Verify that user is not authorized after removing cookies
    """
    session.delete_cookie('token')
    login_page = LoginPage(session)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    session.delete_cookie('token')
    books = BooksPage(session)
    books.open()
    with pytest.raises(NoSuchElementException):
        books.get_displayed_username()
