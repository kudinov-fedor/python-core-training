from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from python_at_2021.tests.akaiafiuk.constants import LOGIN
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.page import Page
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.login_page import LoginPage
from python_at_2021.tests.akaiafiuk.book_store_ui.elements.books_table import BooksTable


class BooksPage(Page):
    url = '/books'

    PAGE_TITLE = By.CSS_SELECTOR, '.main-header'
    LOGIN_BUTTON = By.CSS_SELECTOR, '#login'
    USER_NAME = By.CSS_SELECTOR, '#userName-value'
    SEARCH_INPUT = By.CSS_SELECTOR, '#searchBox'

    def get_books_table(self) -> BooksTable:
        return BooksTable(self.session)

    def click_login(self) -> LoginPage:
        self.element(BooksPage.LOGIN_BUTTON).click()
        return LoginPage(self.session)

    def get_displayed_username(self) -> str:
        return self.element(BooksPage.USER_NAME).text

    def user_is_logged_in(self) -> bool:
        return LOGIN in self.session.page_source

    def do_search(self, search_text: str) -> WebDriver:
        """
        Execute search on the page
        :param search_text: Search criteria
        :return: None
        """
        search_input = self.element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_text)
        search_input.send_keys(Keys.ENTER)
        return self
