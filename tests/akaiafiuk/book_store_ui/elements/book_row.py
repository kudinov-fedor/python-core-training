from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.book_store_ui.elements.base_element import BaseElement
from selenium.webdriver.remote.webdriver import WebElement


class BookRow(BaseElement):
    BOOK_TITLE = By.XPATH, './/a'
    BOOK_AUTHOR = By.XPATH, './div[3]'
    BOOKS_IMAGE = By.XPATH, './/img'
    BOOKS_LINK = By.XPATH, './/a'

    @property
    def title(self) -> str:
        """
        Returns a string with a book title for a specific row
        :return: string with a book title
        """
        return self.element(BookRow.BOOK_TITLE).text

    @property
    def author(self) -> str:
        """
        Returns a string with a book author for a specific row
        :return: string with a book author
        """
        return self.element(BookRow.BOOK_AUTHOR).text

    @property
    def image(self) -> WebElement:
        return self.element(BookRow.BOOKS_IMAGE)

    @property
    def link(self) -> WebElement:
        return self.element(BookRow.BOOKS_LINK)
