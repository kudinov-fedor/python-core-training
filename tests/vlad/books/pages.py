from typing import List

from .constants import USER, PASSWORD

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    HOST = "https://demoqa.com"
    URL = ""
    TIMEOUT = 10

    LOGOUT_BTN = "//div[@id='books-wrapper']//button[@id='submit']"
    HEADER_LOCATOR = ".main-header"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def open(self):
        self.driver.get(self.HOST + self.URL)
        return self.wait_page_loaded

    @property
    def header(self):
        return self.find_element(By.CSS_SELECTOR, self.HEADER_LOCATOR).text

    @property
    def wait(self) -> Wait:
        return Wait(self.driver, self.TIMEOUT)

    @property
    def wait_page_loaded(self):
        self.wait.until(EC.url_contains(self.URL))
        return self

    def logout(self):
        self.find_element(By.ID, self.LOGOUT_BTN).click()
        return self


class LoginPage(BasePage):
    URL = "/login"
    HEADER = "Login"

    USERNAME = "#userName"
    PASSWORD = "#password"
    LOGIN_BTN = "button#login"

    def login(self, user: str = None, password: str = None):
        userName = self.find_element(By.CSS_SELECTOR, self.USERNAME)
        userName.clear()
        userName.send_keys(user or USER)

        passwordField = self.find_element(By.CSS_SELECTOR, self.PASSWORD)
        passwordField.clear()
        passwordField.send_keys(password or PASSWORD)

        self.find_element(By.CSS_SELECTOR, self.LOGIN_BTN).click()
        return ProfilePage(self.driver).wait_page_loaded

    def logout(self):
        logout_btn = self.find_element(By.CSS_SELECTOR, self.LOGIN_BTN)
        logout_btn.click()
        return self


class BooksPage(BasePage):
    URL = "/books"
    HEADER = "Book Store"
    BOOK_TABLE_LOCATOR = "#books-wrapper"

    #Search and login header
    USERNAME_LABEL = "#userName-value"
    SEARCH_BOX = "#searchBox"

    # Books table
    BOOK_TABLE_ROWS = ".ReactTable .rt-tbody div[role=row]"
    BOOKS_LINKS = BOOK_TABLE_ROWS + " a"
    BOOKS_ROWS = "//div[contains(@class,'books-wrapper')]//div[@role='row']//a//ancestor::div[@role='row']"

    @property
    def book_table(self):
        return self.find_element(By.CSS_SELECTOR, self.BOOK_TABLE_LOCATOR)

    def get_books_links(self):
        return self.book_table.find_elements_by_css_selector(self.BOOKS_LINKS)


class ProfilePage(BooksPage):
    URL = "/profile"
    HEADER = "Profile"
    BOOK_TABLE_LOCATOR = "div.profile-wrapper"

    #Pagination section
    PAGINATION_PREVIOUS_BTN = ".pagination-bottom .-previous button"
    PAGINATION_NEXT_BTN = ".pagination-bottom .-next button"
    PAGINATION_PAGE_INPUT = ".pagination-bottom input[type=number]"
    PAGINATION_ROW_PER_PAGE = ".pagination-bottom select"

    # Bottom control buttons
    GO_TO_STORE_BTN = "button#gotoStore"
    DELETE_ACCOUNT_BTN = ".buttonWrap .text-center [id='submit']"
    DELETE_ALL_BOOKS_BTN = ".buttonWrap .text-right [id='submit']"

    def select_pagination_row_per_page_value(self, text):
        row_per_page = Select(self.find_element(By.CSS_SELECTOR, self.PAGINATION_ROW_PER_PAGE))
        row_per_page.select_by_visible_text(text)
        return self

    def get_book_tables_rows(self):
        return self.book_table.find_elements_by_css_selector(self.BOOK_TABLE_ROWS)


class BookPage(BasePage):
    URL = "/books"
    HEADER = "Book Store"

    #Book info
    ISBN = "//*[@id='ISBN-label']/parent::div/following-sibling::div/label"
    TITLE = "//*[@id='title-label']/parent::div/following-sibling::div/label"
    SUB_TITLE = "//*[@id='subtitle-label']/parent::div/following-sibling::div/label"
    AUTHOR = "//*[@id='author-label']/parent::div/following-sibling::div/label"
    PUBLISHER = "//*[@id='publisher-label']/parent::div/following-sibling::div/label"
    TOTAL_PAGES = "//*[@id='pages-label']/parent::div/following-sibling::div/label"
    DESCRIPTION = "//*[@id='description-label']/parent::div/following-sibling::div/label"
    WEBSITE = "//*[@id='website-label']/parent::div/following-sibling::div/label"

    #Bottom buttons
    BACK_BTN = ".fullButtonWrap .text-left"
    ADD_TO_COLLECTION_BTN = ".fullButtonWrap .text-right"