import time
import pytest
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

BOOKS_DEMO_URL = 'https://demoqa.com/books'

SEARCH_BOX = (By.ID, 'searchBox')
SEARCH_BUTTON = (By.ID, 'basic-addon2')
PAGES_SELECT = (By.XPATH, '//select[@aria-label="rows per page"]')
PREV_BUTTON = (By.XPATH, '//div[@class="-previous"]//button')
NEXT_BUTTON = (By.XPATH, '//div[@class="-next"]//button')
CURRENT_PAGE_INPUT = (By.XPATH, '//span[@class="-pageInfo"]//input')
TOTAL_PAGES_LABEL = (By.CSS_SELECTOR, '.-totalPages')
BOOKS_TABLE = (By.XPATH, '//div[@class="rt-table"]')
TABLE_ROW_EMPTY = (By.XPATH, '//div[contains(@class, "rt-tr -padRow")]')
TABLE_ROW_DATA = (By.XPATH, '//div[contains(@class, "rt-tr -odd") or contains(@class, "rt-tr -even")]')
COLUMN_XPATH = '//div[@class="rt-tr-group"][{}]//div[@class="rt-td"][{}]'


def get_values_by_column_number(driver, table_locator, column_number):
    column_values = []
    data_rows = table_locator.find_elements(*TABLE_ROW_DATA)
    for n in range(1, len(data_rows) + 1):
        column_text = driver.find_element(By.XPATH, COLUMN_XPATH.format(n, column_number)).text
        column_values.append(column_text)
    return column_values


def test_next_button_enabled_if_next_page_exist(driver):
    driver.get(BOOKS_DEMO_URL)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    page_selector = Select(driver.find_element(*PAGES_SELECT))
    page_selector.select_by_value('5')
    current_page_num = driver.find_element(*CURRENT_PAGE_INPUT).get_attribute('value')
    total_page_num = driver.find_element(*TOTAL_PAGES_LABEL).text
    is_next_button_disabled = driver.find_element(*NEXT_BUTTON).get_attribute('disabled')
    assert int(current_page_num) == 1
    assert int(total_page_num) > int(current_page_num)
    assert is_next_button_disabled is None


@pytest.mark.parametrize("number_of_pages", [(5), (10), (20)])
def test_select_rows_per_page(driver, number_of_pages):
    driver.get(BOOKS_DEMO_URL)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    page_selector = Select(driver.find_element(*PAGES_SELECT))
    page_selector.select_by_value(str(number_of_pages))
    books_table = driver.find_element(*BOOKS_TABLE)
    empty_rows = books_table.find_elements(*TABLE_ROW_EMPTY)
    data_rows = books_table.find_elements(*TABLE_ROW_DATA)
    assert len(empty_rows) + len(data_rows) == number_of_pages


@pytest.mark.parametrize("filter_value, column_number, filtered_books_count", [
    ("No Starch Press", 4, 2),
    ("Javascript", 2, 4)
])
def test_filter_books_by_value(driver, filter_value, filtered_books_count, column_number):
    driver.get(BOOKS_DEMO_URL)
    search_box = driver.find_element(*SEARCH_BOX)
    search_box.clear()
    search_box.send_keys(filter_value)
    search_box.send_keys(Keys.ENTER)
    books_table = driver.find_element(*BOOKS_TABLE)
    data_rows = books_table.find_elements(*TABLE_ROW_DATA)
    filtered_columns = get_values_by_column_number(driver, books_table, column_number)
    assert len(data_rows) == filtered_books_count
    assert all(filter_value.lower() in cell_text.lower() for cell_text in filtered_columns) == True
