from typing import List
from selenium.webdriver.common.by import By

from automationpractice.constants import EMAIL, PASSWORD
from selenium_helpers.base_page_object import BasePage as _BasePage, GetItem, GetItems, BaseElement


class CartElement(BaseElement):

    class Locator:
        item = By.CSS_SELECTOR, ".remove_link"

    products = GetItems(By.CSS_SELECTOR, ".products dt")
    cart_quantity = GetItem(By.CSS_SELECTOR, ".ajax_cart_quantity")

    @property
    def is_empty(self) -> bool:
        return self.cart_quantity.text == "0"

    # todo
    def remove_all(self):
        if self.is_empty:
            return

        ac = self.ac.move_to_element(self.driver)

        # self.do_hover()

        for item in self.products:
            ac.click(item.find_element(*self.Locator.item))
            # item.find_element(*self.Locator.item).click()
        ac.perform()


class BasePage(_BasePage):

    host = "http://automationpractice.com"

    header_user_info = GetItem(By.CSS_SELECTOR, ".header_user_info a")
    shopping_cart: CartElement = GetItem(By.CSS_SELECTOR, ".shopping_cart", factory=CartElement)
    search_query_top = GetItem(By.CSS_SELECTOR, "#search_query_top")
    block_top_menu = GetItem(By.CSS_SELECTOR, "#block_top_menu")   # categories

    @property
    def user_is_logged_in(self) -> bool:
        return self.header_user_info.get_property("class") == "login"

    def log_out(self):
        if self.user_is_logged_in:
            self.header_user_info.click()
        # todo return page

    def search(self, value):
        search_query_top = self.search_query_top
        search_query_top.send_keys(value)
        search_query_top.submit()
        return ItemsPage(self.driver)


class MainPage(BasePage):

    url = "/index.php"
    title = "My Store"

    home_page_tabs = GetItem(By.CSS_SELECTOR, "#home-page-tabs")
    homefeatured = GetItem(By.CSS_SELECTOR, "#homefeatured")


class SignInPage(BasePage):

    url = "/index.php?controller=authentication&back=my-account"
    title = "Login - My Store"

    login_email = GetItem(By.CSS_SELECTOR, "#email")
    login_passwd = GetItem(By.CSS_SELECTOR, "#passwd")
    login_submit = GetItem(By.CSS_SELECTOR, "#SubmitLogin")

    def log_in(self, email: str = None, password: str = None):
        self.login_email.send_keys(email or EMAIL)
        self.login_passwd.send_keys(password or PASSWORD)
        self.login_submit.click()
        return  # ProfilePage


class AddToCartPopUp(BaseElement):
    to_checkout_btn = GetItem(By.CSS_SELECTOR, ".button-container [title='Proceed to checkout']")
    continue_shopping_btn = GetItem(By.CSS_SELECTOR, ".button-container [title='Continue shopping']")


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
