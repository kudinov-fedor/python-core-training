from selenium.webdriver.common.by import By


class BooksLocators:
    PAGE_TITLE = By.CSS_SELECTOR, '.main-header'
    SEARCH_INPUT = By.CSS_SELECTOR, '#searchBox'
    SEARCH_ICON = By.CSS_SELECTOR, '.input-group-text'
    LOGIN_BUTTON = By.CSS_SELECTOR, '#login'

    COLUMN_TITLES = By.XPATH, '//*[@class="rt-resizable-header-content"]'
    BOOK_TITLES = By.XPATH, '//*[contains(@class, "action")]/*/a'
    TABLE_ROW = By.XPATH, '//*[@class="action-buttons"]/ancestor::*[@role="row"]'
    BOOK_TITLE = By.XPATH, '/following::a'
    BOOK_AUTHOR = By.XPATH, '/div[3]'

    @staticmethod
    def get_book_locator_locator_by_name(name):
        return f'//*[text() = "{name}"]'
