from selenium.webdriver.common.by import By


class BooksLocators:
    PAGE_TITLE = By.CSS_SELECTOR, 'body > #app .pattern-backgound .main-header'
    SEARCH_INPUT = By.CSS_SELECTOR, '#searchBox'
    SEARCH_ICON = By.CSS_SELECTOR, '.input-group-text'
    LOGIN_BUTTON = By.CSS_SELECTOR, '[type="button"]'

    COLUMN_TITLES = By.XPATH, './/*[@class="rt-resizable-header-content"]'
    BOOK_TITLES = By.XPATH, './/*[contains(@class, "action")]/*/a'
    BOOK_AUTHORS = By.XPATH, './/div[3][@class="rt-td"]'
    TABLE_ROW = By.XPATH, './/*[@class="rt-tr-group"]/child::*'
