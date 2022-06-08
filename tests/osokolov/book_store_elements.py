
from selenium.webdriver.common.by import By


class BookStoreElements:
    def __init__(self):

        self.search_box = (By.XPATH, '//input[@id="searchBox"]')
        self.login_button = (By.XPATH, '//button[@id="login"]')

        self.headers = (By.XPATH, '//div[@class="rt-thead -header"]/div[@class="rt-tr"]')
        self.image = (By.XPATH, f'{self.headers[1]}/div[1]')
        self.title = (By.XPATH, f'{self.headers[1]}/div[2]')
        self.author = (By.XPATH, f'{self.headers[1]}/div[3]')
        self.publisher = (By.XPATH, f'{self.headers[1]}/div[4]')

        self.table_rows = (By.XPATH, '//div[@class="rt-tr-group"]//img')
        self.table_row = lambda row_number: (By.XPATH, f'//div[@class="rt-tbody"]//div[@class="rt-tr-group"][{row_number}]')

        self.page_field = (By.XPATH, '//input[@aria-label="jump to page"]')
