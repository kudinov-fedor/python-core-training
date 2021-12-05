from typing import List
from selenium.webdriver.common.by import By

from selenium_helpers.base_page_object import BasePage as _BasePage, GetItem, GetItems, BaseElement


class BasePage(_BasePage):
    host = "http://automationpractice.com"


class CartDropDown(BaseElement):

    products = GetItems(By.CSS_SELECTOR, ".products dt")

    # todo does not work
    def remove_all(self):
        self.do_hover()
        for item in self.products:
            item.find_element(By.CSS_SELECTOR, ".remove_link").click()


class MainPage(BasePage):

    url = "/index.php"
    title = "My Store"

    block_top_menu = GetItem(By.CSS_SELECTOR, "#block_top_menu")
    shopping_cart = GetItem(By.CSS_SELECTOR, ".shopping_cart", factory=CartDropDown)
    search_query_top = GetItem(By.CSS_SELECTOR, "#search_query_top")
    homefeatured = GetItem(By.CSS_SELECTOR, "#homefeatured")
    home_page_tabs = GetItem(By.CSS_SELECTOR, "#home-page-tabs")
    header = GetItem(By.CSS_SELECTOR, "#header")

    def search(self, value):
        search_query_top = self.search_query_top
        search_query_top.send_keys(value)
        search_query_top.submit()
        return ItemsPage(self.driver)


class AddToCartPopUp(BaseElement):
    to_checkout_btn = GetItem(By.CSS_SELECTOR, ".button-container [title='Proceed to checkout']")


class Item(BaseElement):
    product_name = GetItem(By.CSS_SELECTOR, "a.product-name")
    add_to_cart_button = GetItem(By.CSS_SELECTOR, "a.button.ajax_add_to_cart_button")
    layer_cart: AddToCartPopUp = GetItem(By.CSS_SELECTOR, "#layer_cart", factory=AddToCartPopUp, from_parent=True)

    def title(self):
        return self.product_name.text

    def add_to_cart(self):
        self.do_hover()
        self.add_to_cart_button.click()
        return self.layer_cart


class ItemsPage(BasePage):

    title = "Search - My Store"

    left_column = GetItem(By.CSS_SELECTOR, "#left_column")
    center_column = GetItem(By.CSS_SELECTOR, "#center_column")
    products: List[Item] = GetItems(By.CSS_SELECTOR, "#center_column .product_list .product-container", factory=Item)


class OrderItem(BaseElement):
    delete_item = GetItem(By.CSS_SELECTOR, ".cart_quantity_delete")


class OrderPage(BasePage):

    url = "/index.php?controller=order"
    title = "Order - My Store"

    cart_items: List[OrderItem] = GetItems(By.CSS_SELECTOR, "#cart_summary tbody tr", factory=OrderItem)

    # todo finish
    def cart_is_empty(self):
        return
