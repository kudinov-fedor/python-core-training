from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from page_object.pages.base_page import BasePage


class BookPage(BasePage):
    BACK_TO_BOOKSTORE_BUTTON = '//button[text()="Back To Book Store"]'
    ADD_TO_YOUR_COLLECTION_BUTTON = '//button[text()="Add To Your Collection"]'

    def add_book_to_collection(self):
        self.find_element(By.XPATH, self.ADD_TO_YOUR_COLLECTION_BUTTON).click()
        Wait(self.driver, 2).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def cleanup(self):
        ...
