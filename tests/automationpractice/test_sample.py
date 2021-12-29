import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from automationpractice import BasePage, MainPage, OrderPage, SignInPage


@pytest.fixture
def flush_cart(session):
    yield
    shopping_cart = MainPage(session).open_page().shopping_cart
    shopping_cart.remove_all()
    assert shopping_cart.is_empty


@pytest.fixture(autouse=True)
def logout(session: WebDriver):
    yield
    BasePage(session).log_out()


def test_user_not_logged_in(session: WebDriver):
    main = MainPage(session).open_page()
    assert not main.user_is_logged_in


def test_login(session: WebDriver):

    SignInPage(session)\
        .open_page()\
        .log_in()


def test_cart_is_empty(session: WebDriver):
    assert OrderPage(session).open_page().shopping_cart.is_empty


def test_search_flow(session: WebDriver):

    main = MainPage(session).open_page()
    assert not main.user_is_logged_in

    products = main.search("Dress").products
    assert len(products) == 7


def test_add_to_cart_from_search(session: WebDriver, flush_cart):

    main = MainPage(session).open_page()

    search_page = main.search("Dress")
    assert len(search_page.products) == 7

    search_page.products[3].add_to_cart().continue_shopping_btn.click()
    search_page.products[2].add_to_cart().continue_shopping_btn.click()

    assert len(OrderPage(session).open_page().cart_items) == 2


def test_clean_order(session: WebDriver):
    main = MainPage(session).open_page()

    search_page = main.search("Dress")
    assert len(search_page.products) == 7

    search_page.products[3].add_to_cart().continue_shopping_btn.click()
    search_page.products[2].add_to_cart().continue_shopping_btn.click()

    order_page = OrderPage(session).open_page()
    assert len(order_page.cart_items) == 2

    for item in order_page.cart_items:
        item.delete_item.click()

    assert order_page.shopping_cart.is_empty
