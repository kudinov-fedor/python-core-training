from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from python_at_2021.tests.akaiafiuk.constants import LOGIN
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.page import Page
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.login_page import LoginPage


class BooksPage(Page):
    url = '/books'

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
        return self

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

    def click_login(self) -> LoginPage:
        self.session.find_element(*BooksPage.LOGIN_BUTTON).click()
        return LoginPage(self.session)

    def get_displayed_username(self) -> str:
        return self.session.find_element(*BooksPage.USER_NAME).text

    def user_is_logged_in(self) -> bool:
        return LOGIN in self.session.page_source
