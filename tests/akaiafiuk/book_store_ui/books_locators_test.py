from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.constants import HOST


class BooksLocators:
    PAGE_TITLE = By.CSS_SELECTOR, '.main-header'
    SEARCH_INPUT = By.CSS_SELECTOR, '#searchBox'
    SEARCH_ICON = By.CSS_SELECTOR, '.input-group-text'
    LOGIN_BUTTON = By.CSS_SELECTOR, '#login'

    COLUMN_TITLES = By.XPATH, '//*[@class="rt-resizable-header-content"]'
    TABLE_ROW = By.XPATH, '//*[@class="action-buttons"]/ancestor::*[@role="row"]'
    BOOK_TITLE = By.XPATH, './/a'
    BOOK_AUTHOR = By.XPATH, './div[3]'

    @staticmethod
    def get_book_locator_by_name(name):
        return f'//*[text() = "{name}"]'


def test_locators(session):
    session.get(HOST + '/books')
    row = session.find_elements(*BooksLocators.TABLE_ROW)[0]
    title = row.find_element(*BooksLocators.BOOK_TITLE)
    author = row.find_element(*BooksLocators.BOOK_AUTHOR)
    assert title.text == 'Git Pocket Guide'
    assert 'Richard E.' in author.text
