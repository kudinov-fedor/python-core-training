import pytest
import requests
from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.constants import HOST
from selenium.webdriver.common.keys import Keys


class BooksLocators:
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

    @staticmethod
    def get_book_locator_by_name(name):
        return f'//*[text() = "{name}"]'


@pytest.mark.books
def test_locators(session):
    """
    Verify that locators are correct and it is possible to test a separate table row
    """
    session.get(HOST + '/books')
    row = session.find_elements(*BooksLocators.TABLE_ROW)[0]
    title = row.find_element(*BooksLocators.BOOK_TITLE)
    author = row.find_element(*BooksLocators.BOOK_AUTHOR)
    assert title.text == 'Git Pocket Guide'
    assert 'Richard E.' in author.text


@pytest.mark.books
def test_search(bookstore_session):
    """
    Test search using exact match
    """
    row = bookstore_session.find_elements(*BooksLocators.TABLE_ROW)[0]
    title = row.find_element(*BooksLocators.BOOK_TITLE)
    search_input = bookstore_session.find_element(*BooksLocators.SEARCH_INPUT)
    search_input.send_keys(title.text)
    search_input.send_keys(Keys.ENTER)
    rows = bookstore_session.find_elements(*BooksLocators.TABLE_ROW)
    assert len(rows) == 1


@pytest.mark.books
def test_column_names(bookstore_session):
    """
    Test that column names are correct
    """
    expected_titles = ('Image', 'Title', 'Author', 'Publisher')
    columns = bookstore_session.find_elements(*BooksLocators.COLUMN_TITLES)
    assert len(columns) == len(expected_titles)
    assert all(text.text in expected_titles for text in columns)


@pytest.mark.books
def test_books_images(bookstore_session):
    """
    Test that a valid image is displayed for each book
    """
    rows = bookstore_session.find_elements(*BooksLocators.TABLE_ROW)
    images = list(row.find_element(*BooksLocators.BOOKS_IMAGES) for row in rows)
    for i in images:
        link = i.get_attribute('src')
        r = requests.head(link)
        assert r.headers['Content-Type'] == 'image/jpeg'


@pytest.mark.books
def test_books_links(bookstore_session):
    """
    Test that bok links are not broken
    """
    rows = bookstore_session.find_elements(*BooksLocators.TABLE_ROW)
    links = list(row.find_element(*BooksLocators.BOOKS_LINKS) for row in rows)
    for i in links:
        link = i.get_attribute('href')
        r = requests.head(link)
        assert 200 <= r.status_code < 400
        r.raise_for_status()
