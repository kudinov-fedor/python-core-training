import pytest
import time

from selenium.webdriver.remote.webdriver import WebDriver, By


@pytest.mark.parametrize("search, expected_count", [
    ("", 6),
    ("mAnAgeR", 6),
    ("234-", 2),
    ("-234-", 1)
])
def test_data_filter(session: WebDriver, search, expected_count):
    session.get("https://www.seleniumeasy.com/test/data-list-filter-demo.html")

    session.find_element(By.ID, "input-search").send_keys(search)
    items = [i for i in session.find_elements(By.CSS_SELECTOR, '.items')
             if i.value_of_css_property("display") == 'block']
    assert len(items) == expected_count
    assert all(search.lower() in i.text.lower() for i in items)
