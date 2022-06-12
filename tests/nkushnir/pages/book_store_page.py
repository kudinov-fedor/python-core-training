from selenium.webdriver.common.by import By
from tests.nkushnir.pages.base_page import BasePage


class BookStorePage(BasePage):
    PAGE_PATH = 'books'
    COLUMNS = {"image": 1, "title": 2, "author": 3, "publisher": 4}
    SEARCH_BOX = (By.ID, 'searchBox')
    SEARCH_BUTTON = (By.ID, 'basic-addon2')
    PAGES_SELECT = (By.XPATH, '//select[@aria-label="rows per page"]')
    PREV_BUTTON = (By.XPATH, '//div[@class="-previous"]//button')
    NEXT_BUTTON = (By.XPATH, '//div[@class="-next"]//button')
    CURRENT_PAGE_INPUT = (By.XPATH, '//span[@class="-pageInfo"]//input')
    TOTAL_PAGES_LABEL = (By.CSS_SELECTOR, '.-totalPages')
    BOOKS_TABLE = (By.XPATH, '//div[@class="rt-table"]')
    TABLE_ROW = (By.XPATH, '//div[contains(@class, "rt-tr-group")]')
    TABLE_ROW_EMPTY = (By.XPATH, '//div[contains(@class, "rt-tr -padRow")]')
    TABLE_ROW_DATA = (By.XPATH, '//div[contains(@class, "rt-tr -odd") or contains(@class, "rt-tr -even")]')
    CELL_XPATH = '//div[@class="rt-td"][{}]'


    def open(self):
        self.open_page(self.PAGE_PATH)

    def select_table_rows_number(self, rows_number):
        self.select_by_value(self.PAGES_SELECT, rows_number)
    
    def get_current_page_number(self):
        return int(self.get_attr(self.CURRENT_PAGE_INPUT, 'value'))
    
    def get_total_pages_number(self):
        return int(self.get_text(self.TOTAL_PAGES_LABEL))
    
    def next_page_is_enabled(self):
        return self.is_enabled(self.NEXT_BUTTON)
    
    def get_table_rows_number(self):
        return self.get_elements_length(self.TABLE_ROW)
    
    def search_book_by_value(self, value_to_enter):
        self.enter_text(self.SEARCH_BOX, value_to_enter)
        self.confirm_by_enter(self.SEARCH_BOX)
    
    def get_table_rows_with_data_number(self):
        return self.get_elements_length(self.TABLE_ROW_DATA)
    
    def get_values_from_column(self, column):
        column_values = []
        for row in self.get_elements_list(self.TABLE_ROW_DATA):
            col_locator = self.format_xpath_locator(self.CELL_XPATH, self.COLUMNS[column.lower()])
            cell_text = self.get_text_by_parent(row, col_locator)
            column_values.append(cell_text)
        return column_values
    
    def table_is_filtered_by_column_value(self, filter_value, column):
        column_values = self.get_values_from_column(column)
        return all(filter_value.lower() in cell_text.lower() for cell_text in column_values)
    