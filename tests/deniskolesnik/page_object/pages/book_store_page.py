from selenium.webdriver.common.by import By

from page_object.pages.base_page import BasePage


class BookStore(BasePage):
    URL = '/books'
    BOOKS = '.rt-tr-group'
    SEARCH_FIELD = '#searchBox'

    def search_book_and_open(self, book_name):
        search_field = self.find_element(By.CSS_SELECTOR, self.SEARCH_FIELD)
        search_field.send_keys(book_name)
        book = self.find_element(By.XPATH, '//a[text()="{}"]'.format(book_name))
        book_link = book.get_attribute('href')
        book.click()
        return book_link
