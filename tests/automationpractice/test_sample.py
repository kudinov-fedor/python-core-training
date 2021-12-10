import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from automationpractice import BasePage, MainPage, OrderPage, SignInPage


@pytest.fixture
def flush_cart(session):
    yield
    # MainPage(session).open_page().shopping_cart.remove_all()  # todo
    for item in OrderPage(session).open_page().cart_items:
        item.delete_item.click()
    assert OrderPage(session).open_page().shopping_cart.is_empty


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


def test_search_flow(session: WebDriver):

    main = MainPage(session).open_page()
    assert not main.user_is_logged_in

    products = main.search("Dress").products
    assert len(products) == 7


def test_add_to_cart_from_search(session: WebDriver, flush_cart):

    main = MainPage(session).open_page()
    assert not main.user_is_logged_in

    products = main.search("Dress").products
    assert len(products) == 7

    products[3].add_to_cart().continue_shopping_btn.click()
    products[2].add_to_cart().continue_shopping_btn.click()

    assert len(OrderPage(session).open_page().cart_items) == 2
