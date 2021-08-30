from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from ui_testing.wiki_page_object.pages import MainPage


def test_sample(session: WebDriver):

    page = MainPage(session)
    page.open_page()
    search_page = page.do_search("some text")
    search_page.get_title()

    results = search_page.get_search_results()

    for r in results:
        print(r.get_title())

    sleep(10)
