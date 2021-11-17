from typing import List

from selenium.webdriver.common.by import By

from ui_testing.page_object.base_page_object import BaseElement, BasePage as _BasePage


class BasePage(_BasePage):
    host = "https://en.wikipedia.org/"


class MainPage(BasePage):

    url = "wiki/Main_Page"
    title = "Wikipedia, the free encyclopedia"

    SEARCH_INPUT = By.ID, "searchInput"
    SEARCH_BTN = By.ID, "searchButton"

    def do_search(self, text) -> 'SearchPage':
        self.do_send_keys(self.SEARCH_INPUT, text)
        self.do_click(self.SEARCH_BTN)
        return SearchPage(self.driver)


class SearchPage(BasePage):

    url = "wiki/Main_Page"
    title = "- Search results - Wikipedia"

    SEARCH_RESULTS = By.CLASS_NAME, "mw-search-results"
    SEARCH_RESULT = By.CLASS_NAME, "mw-search-result"

    def get_search_results(self) -> List['SearchResult']:
        el = self.get_element(self.SEARCH_RESULTS)
        els = el.find_elements(*self.SEARCH_RESULT)
        return [SearchResult(el) for el in els]


class SearchResult(BaseElement):

    SEARCH_RESULT_HEADING = By.CLASS_NAME, "searchresult"

    def get_title(self):
        return self.get_element(self.SEARCH_RESULT_HEADING).text
