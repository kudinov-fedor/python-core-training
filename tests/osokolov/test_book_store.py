from tests.osokolov.book_store_elements import BookStoreElements

HOST = 'https://demoqa.com'


def test_book_store(browser):
    path = '/books'
    browser.get(f'{HOST}{path}')
    book_store = BookStoreElements()

    image = browser.find_element(*book_store.image).text
    assert image == "Image"

    table = browser.find_elements(*book_store.table_rows)
    assert len(table) == 10
