
from selenium.webdriver.common.by import By


class BookStoreElements:
    def __init__(self, browser):
        self.browser = browser

        self.search_box = self.browser.find_element(By.XPATH, '//input[@id="searchBox"]')
        self.login_button = self.browser.find_element(By.XPATH, '//button[@id="login"]')

        self.headers = self.browser.find_element(By.XPATH, '//div[@class="rt-thead -header"]/div[@class="rt-tr"]')
        self.image = self.headers.find_element(By.XPATH, './/*[contains(text(), "Image")]')
        self.title = self.headers.find_element(By.XPATH, './/*[contains(text(), "Title")]')
        self.author = self.headers.find_element(By.XPATH, './/*[contains(text(), "Author")]')
        self.publisher = self.headers.find_element(By.XPATH, './/*[contains(text(), "Publisher")]')

        self.table_row = lambda row_number: self.browser.find_element(By.XPATH, f'//div[@class="rt-tbody"]//div[@class="rt-tr-group"][{row_number}]')

        self.page_field = self.browser.find_element(By.XPATH, '//input[@aria-label="jump to page"]')
