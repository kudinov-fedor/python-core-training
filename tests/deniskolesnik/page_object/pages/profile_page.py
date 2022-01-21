from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from page_object import env_variable
from page_object.pages.base_page import BasePage


class Profile(BasePage):
    URL = '/profile'
    SEARCH_FIELD = '.searchBox'
    GO_TO_BOOKSTORE_BUTTON = '//button[text()="Go To Book Store"]'
    DELETE_ACCOUNT_BUTTON = '//button[text()="Delete Account"]'
    DELETE_ALL_BOOKS_BUTTON = '//*[contains(@class, "text-right button di")]//button[text()="Delete All Books"]'
    POPUP_OK_BUTTON = '#closeSmallModal-ok'
    DELETE_BOOK_BUTTON = '#delete-record-undefined'
    BOOK = '//a[text()="{}"]'.format(env_variable.BOOK_NAME)
    ACTIONS_BUTTONS = '.action-buttons'

    def delete_all_books(self):
        self.find_element(By.XPATH, self.DELETE_ALL_BOOKS_BUTTON).click()
        self.find_element(By.CSS_SELECTOR, self.POPUP_OK_BUTTON).click()

        Wait(self.driver, 2).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def check_if_books_added(self):
        try:
            self.driver.find_elements(By.CSS_SELECTOR, self.ACTIONS_BUTTONS)
            self.delete_all_books()
        except NoSuchElementException:
            return print('No books added')

    def get_list_of_books(self):
        ...
