import os
import pytest
driver_path = os.environ.get("DRIVER_PATH", "chromedriver")
from selenium.webdriver import Chrome, Firefox, Edge, Opera, Safari, ChromeOptions


@pytest.fixture
def session():
    options = ChromeOptions()
    # options.add_experimental_option('androidPackage', 'com.android.chrome')
    session = Chrome(driver_path, options=options)
    session.maximize_window()
    yield session
    session.quit()


@pytest.mark.parametrize("iterable, expected", [
    ([1, 2, 3], 6),
    ([True, False, True], 2),
    ([5], 5),
])
def test_sum(iterable, expected):
    assert sum(iterable) == expected


@pytest.mark.parametrize("item, error", [
    (["a", "b", "c"], TypeError),
    (5, TypeError),
])
def test_sum_error(item, error):
    with pytest.raises(error):
        sum(item)
