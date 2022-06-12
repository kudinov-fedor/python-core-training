import pytest
from tests.nkushnir.pages.book_store_page import BookStorePage


def test_next_button_enabled_if_next_page_exist(driver):
    book_store_page = BookStorePage(driver)
    book_store_page.open()
    book_store_page.scroll_to_bottom()
    book_store_page.select_table_rows_number(5)
    assert book_store_page.get_current_page_number() == 1
    assert book_store_page.get_total_pages_number() > book_store_page.get_current_page_number()
    assert book_store_page.next_page_is_enabled() == True


@pytest.mark.parametrize("number_of_pages", [(5), (10), (20)])
def test_select_rows_per_page(driver, number_of_pages):
    book_store_page = BookStorePage(driver)
    book_store_page.open()
    book_store_page.scroll_to_bottom()
    book_store_page.select_table_rows_number(number_of_pages)
    assert book_store_page.get_table_rows_number() == number_of_pages


@pytest.mark.parametrize("filter_value, column, filtered_books_count", [
    ("No Starch Press", "Publisher", 2),
    ("Javascript", "Title", 4)
])
def test_filter_books_by_value(driver, filter_value, filtered_books_count, column):
    book_store_page = BookStorePage(driver)
    book_store_page.open()
    book_store_page.search_book_by_value(filter_value)
    assert book_store_page.get_table_rows_with_data_number() == filtered_books_count
    assert book_store_page.table_is_filtered_by_column_value(filter_value, column) == True
