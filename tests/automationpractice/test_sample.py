import pytest
from automationpractice import MainPage, OrderPage


@pytest.fixture
def flush_cart(session):
    yield
    for item in OrderPage(session).open_page().cart_items:
        item.delete_item.click()


def test_search_flow(session, flush_cart):
    products = MainPage(session)\
        .open_page()\
        .search("Dress")\
        .products

    assert len(products) == 7

    products[3].add_to_cart()\
        .to_checkout_btn.click()

    MainPage(session) \
        .open_page() \
        .search("Dress") \
        .products[2].add_to_cart() \
        .to_checkout_btn.click()

    assert len(OrderPage(session).open_page().cart_items) == 2
