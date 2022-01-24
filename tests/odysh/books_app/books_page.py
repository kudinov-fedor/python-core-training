from .base_page import BasePage
from .locators import BooksPageLocators

from selenium.webdriver.remote.webdriver import By


class BooksPage(BasePage):
    URL = "/books"
    HEADER = "Book Store"

    def search_book(self):
        search_field = self.find_element(By.ID, BooksPageLocators.search_book_field)
        search_field.send_keys('git pocket')
        return self.find_element(By.ID, BooksPageLocators.git_book).text
