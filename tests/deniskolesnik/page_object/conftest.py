import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def driver_init():
    # add_argument("--ignore-certificate-errors")
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield driver

    driver.quit()
'''
Cleanup Fixture

@pytest.fixture(scope='function')
def clean_books_added(driver_init):
    delete_books = Profile(driver_init).open().delete_all_books()
    assert 'All Books deleted.' in delete_books
'''
