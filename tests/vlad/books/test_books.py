import pytest

from .pages import ProfilePage

def test_pagination_dropdown(login):
    profile_page = ProfilePage(login)
    profile_page.select_pagination_row_per_page_value("10 rows")
    assert len(profile_page.get_book_tables_rows()) == 10
