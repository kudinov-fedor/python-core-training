from selenium.webdriver.common.by import By

from selenium_helpers.base_page_object import BasePage as _BasePage, GetItem


class BasePage(_BasePage):
    host = "http://automationpractice.com"


class MainPage(BasePage):

    url = "/index.php"
    title = "My Store"

    block_top_menu = GetItem(By.CSS_SELECTOR, "#block_top_menu")
    shopping_cart = GetItem(By.CSS_SELECTOR, ".shopping_cart")
    search_query_top = GetItem(By.CSS_SELECTOR, "#search_query_top")
    homefeatured = GetItem(By.CSS_SELECTOR, "#homefeatured")
    home_page_tabs = GetItem(By.CSS_SELECTOR, "#home-page-tabs")
    header = GetItem(By.CSS_SELECTOR, "#header")
