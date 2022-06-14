from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from python_at_2021.tests.akaiafiuk.constants import LOGIN
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.page import Page
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.login_page import LoginPage
from python_at_2021.tests.akaiafiuk.book_store_ui.elements.books_table import BooksTable


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

    def get_books_table(self) -> BooksTable:
        return BooksTable(self.session)

    def do_search(self, search_text: str) -> None:
        """
        Execute search on the page
        :param search_text: Search criteria
        :return: None
        """
        search_input = self.element(BooksPage.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_text)
        search_input.send_keys(Keys.ENTER)
        return self

    def get_images(self) -> list:
        """
        Get a list with all images from the books table
        :return: list of Web Elements
        """
        rows = self.elements(BooksPage.TABLE_ROW)
        images = list(row.find_element(*BooksPage.BOOKS_IMAGES) for row in rows)
        return images

    def get_links(self) -> list:
        """
        Get a list with all links from the books table
        :return: list of Web Elements
        """
        rows = self.elements(BooksPage.TABLE_ROW)
        links = list(row.find_element(*BooksPage.BOOKS_LINKS) for row in rows)
        return links

    def click_login(self) -> LoginPage:
        self.element(BooksPage.LOGIN_BUTTON).click()
        return LoginPage(self.session)

    def get_displayed_username(self) -> str:
        return self.element(BooksPage.USER_NAME).text

    def user_is_logged_in(self) -> bool:
        return LOGIN in self.session.page_source
