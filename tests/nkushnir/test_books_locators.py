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
TABLE_ROW = (By.XPATH, '//div[contains(@class, "rt-tr-group")]')
TABLE_ROW_EMPTY = (By.XPATH, '//div[contains(@class, "rt-tr -padRow")]')
TABLE_ROW_DATA = (By.XPATH, '//div[contains(@class, "rt-tr -odd") or contains(@class, "rt-tr -even")]')
CELL_XPATH = '//div[@class="rt-td"][{}]'


def get_values_by_column_number(data_rows, column_number):
    column_values = []
    for row in data_rows:
        cell_text = row.find_element(By.XPATH, CELL_XPATH.format(column_number)).text
        column_values.append(cell_text)
    return column_values


def test_next_button_enabled_if_next_page_exist(driver):
    driver.get(BOOKS_DEMO_URL)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    page_selector = Select(driver.find_element(*PAGES_SELECT))
    page_selector.select_by_value('5')
    current_page_num = driver.find_element(*CURRENT_PAGE_INPUT).get_attribute('value')
    total_page_num = driver.find_element(*TOTAL_PAGES_LABEL).text
    is_next_button_enabled = driver.find_element(*NEXT_BUTTON).is_enabled()
    assert int(current_page_num) == 1
    assert int(total_page_num) > int(current_page_num)
    assert is_next_button_enabled == True


@pytest.mark.parametrize("number_of_pages", [(5), (10), (20)])
def test_select_rows_per_page(driver, number_of_pages):
    driver.get(BOOKS_DEMO_URL)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    page_selector = Select(driver.find_element(*PAGES_SELECT))
    page_selector.select_by_value(str(number_of_pages))
    books_table = driver.find_element(*BOOKS_TABLE)
    table_rows = books_table.find_elements(*TABLE_ROW)
    assert len(table_rows) == number_of_pages


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
    filtered_columns = get_values_by_column_number(data_rows, column_number)
    assert len(data_rows) == filtered_books_count
    assert all(filter_value.lower() in cell_text.lower() for cell_text in filtered_columns) == True
