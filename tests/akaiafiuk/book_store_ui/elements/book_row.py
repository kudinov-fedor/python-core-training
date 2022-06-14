from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.book_store_ui.elements.base_element import BaseElement


class BookRow(BaseElement):
    BOOK_TITLE = By.XPATH, './/a'
    BOOK_AUTHOR = By.XPATH, './div[3]'

    def get_book_title(self) -> str:
        """
        Returns a string with a book title for a specific row
        :return: string with a book title
        """
        return self.element(BookRow.BOOK_TITLE).text

    def get_book_author(self) -> str:
        """
        Returns a string with a book author for a specific row
        :return: string with a book author
        """
        return self.element(BookRow.BOOK_AUTHOR).text
