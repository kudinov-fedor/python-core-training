from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from page_object import env_variable
from page_object.pages.base_page import BasePage


class Profile(BasePage):
    URL = '/profile'
    search_field = '.searchBox'
    go_to_book_store_button = '//button[text()="Go To Book Store"]'
    delete_account_button = '//button[text()="Delete Account"]'
    delete_all_books_button = '//*[contains(@class, "text-right button di")]//button[text()="Delete All Books"]'
    pop_up_ok_button = '#closeSmallModal-ok'
    delete_book_button = '#delete-record-undefined'
    book = '//a[text()="{}"]'.format(env_variable.BOOK_NAME)

    def delete_all_books(self):
        self.find_element(By.XPATH, self.delete_all_books_button).click()
        self.find_element(By.CSS_SELECTOR, self.pop_up_ok_button).click()

        Wait(self.driver, 2).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def get_list_of_books(self):
        ...
