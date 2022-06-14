from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from python_at_2021.tests.akaiafiuk.book_store_ui.elements.base_element import BaseElement
from python_at_2021.tests.akaiafiuk.book_store_ui.elements.book_row import BookRow


class BooksTable(BaseElement):

    COLUMN_TITLES = By.XPATH, '//*[@class="rt-resizable-header-content"]'
    TABLE_ROW = By.XPATH, '//*[@class="action-buttons"]/ancestor::*[@role="row"]'

    def get_rows(self) -> List[BookRow]:
        """
        Get all book rows currently displayed
        :return: list of Web Elements
        """
        return [BookRow(element) for element in self.elements(BooksTable.TABLE_ROW)]

    def get_columns(self) -> List[WebElement]:
        """
        Get column titles
        :return: list of web elements
        """
        return self.elements(BooksTable.COLUMN_TITLES)
