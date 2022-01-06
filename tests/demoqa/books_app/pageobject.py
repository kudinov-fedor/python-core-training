from typing import List

from .constants import USER, PASSWORD

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    HOST = "https://demoqa.com"
    URL = ""
    HEADER = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def browser_name(self):
        return self.driver.capabilities["browserName"]

    @property
    def platform_name(self):
        return self.driver.capabilities["platformName"]

    @property
    def window_size(self):
        return self.driver.get_window_size()

    def open(self):
        self.driver.get(self.HOST + self.URL)
        return self.on_load

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    @property
    def header(self):
        return self.find_element(By.CSS_SELECTOR, ".main-header").text

    @property
    def on_load(self):
        self.wait.until(EC.url_contains(self.URL))
        return self

    @property
    def wait(self) -> Wait:
        return Wait(self.driver, 10)

    def user_is_loged_in(self):
        ...

    def logout(self):
        raise NotImplementedError


class LoginPage(BasePage):
    URL = "/login"
    HEADER = "Login"

    def login(self, user: str = None, password: str = None):
        userName = self.find_element(By.CSS_SELECTOR, "#userName")
        userName.clear()
        userName.send_keys(user or USER)

        passwordField = self.find_element(By.CSS_SELECTOR, "#password")
        passwordField.clear()
        passwordField.send_keys(password or PASSWORD)

        self.find_element(By.CSS_SELECTOR, "button#login").click()
        return ProfilePage(self.driver).on_load

    def logout(self):
        self.find_element(By.ID, "submit").click()
        return self

    def user_logged_in(self) -> bool:
        ...


class RegisterPage(BasePage):
    ...


class BooksPage(BasePage):
    URL = "/books"
    HEADER = "Book Store"
    BOOK_TABLE_LOCATOR = (By.CSS_SELECTOR, "div.books-wrapper")

    def search(self, value):
        search = self.find_element(By.ID, "searchBox")
        search.clear()
        search.send_keys(value)
        return self

    def user_logged_in(self) -> bool:
        return not self.driver.find_element(By.ID, "notLoggin-wrapper").is_displayed()

    def has_books(self) -> bool:
        books_table = self.find_element(*self.BOOK_TABLE_LOCATOR)
        return "No rows found" not in books_table.text

    def get_books(self):
        if not self.has_books():
            return []
        books_table = self.find_element(*self.BOOK_TABLE_LOCATOR)
        return books_table.find_elements(By.XPATH, "//img/ancestor::div[contains(@class, 'rt-tr-group')]")

    def go_to_book(self, value):
        books = self.get_books()
        if isinstance(value, int):
            book = books[value]
        else:
            raise TypeError
        book.find_element(By.TAG_NAME, "a").click()
        return BookPage(self.driver)

    def logout(self):
        self.find_element(By.ID, "submit").click()
        return LoginPage(self.driver)


class ProfilePage(BooksPage):
    URL = "/profile"
    HEADER = "Profile"
    BOOK_TABLE_LOCATOR = (By.CSS_SELECTOR, "div.profile-wrapper")

    def remove_books(self):
        if not self.has_books():
            return self

        self.find_element(By.CSS_SELECTOR, ".buttonWrap .text-right #submit").click()
        modal = Wait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))
        modal.find_element(By.ID, "closeSmallModal-ok").click()
        alert = Wait(self.driver, 5).until(EC.alert_is_present())
        assert alert.text in ["All Books deleted.", "No books available in your's collection!"]
        alert.accept()
        return self


class BookPage(BasePage):
    ...

    # ISBN
    # Title
    # Sub Title
    # Author
    # Publisher
    # Total Pages
    # Description
    # Website

    # back to book store
    def add_book(self):
        self.on_load.find_element(By.CSS_SELECTOR, ".text-right #addNewRecordButton").click()
        alert = Wait(self.driver, 5).until(EC.alert_is_present())
        assert alert.text in ["Book added to your collection.",
                              "Book already present in the your collection!"]
        alert.accept()


class ProfileBookPage(BasePage):
    ...
