from .base_page import BasePage
from .constants import search_book_field, git_book

from selenium.webdriver.remote.webdriver import By


class BooksPage(BasePage):
    URL = "/books"
    HEADER = "Book Store"

    def search_book(self):
        search_field = self.find_element(By.ID, search_book_field)
        search_field.send_keys('git pocket')
        return self.find_element(By.ID, git_book).text
