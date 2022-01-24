from .base_page import BasePage
from .locators import BooksPageLocators


class BooksPage(BasePage):
    URL = "/books"
    HEADER = "Book Store"

    def search_book(self):
        search_field = self.find_element(*BooksPageLocators.search_book_field)
        search_field.send_keys('git pocket')
        return self.find_element(*BooksPageLocators.git_book).text
