from .constants import USER, PASSWORD

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    HOST = "https://demoqa.com"
    URL = ""
    HEADER = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

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

        self.wait.until(EC.url_changes(self.URL))

        return ProfilePage(self.driver)

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

    # search
    # logout
    # books

    # books on page
    # prev
    # next
    # go to page

    def search(self, value):
        search = self.find_element(By.ID, "searchBox")
        search.clear()
        search.send_keys(value)
        return self

    def get_books(self):
        # rows = self.find_elenents(By.CSS_SELECTOR, ".books-wrapper .rt-tbody .rt-tr-group")
        # return [i for i in rows if i.text.strip(" ")]

        if "No rows found" in self.find_element(By.CLASS_NAME, "books-wrapper").text:
            return []
        return self.find_elements(By.XPATH, "//div[contains(@class, 'books-wrapper')]"
                                            "//img/ancestor::div[contains(@class, 'rt-tr-group')]")


class ProfilePage(BooksPage):
    URL = "/profile"
    HEADER = "Profile"

    # logout
    # search
    # books
    # go to bookstore
    # delete all books
    # delete account

    # books on page
    # open book
    # delete book
    # prev
    # next
    # go to page

    def logout(self):
        self.find_element(By.ID, "submit").click()
        return LoginPage(self.driver)


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


class ProfileBookPage(BasePage):
    ...
