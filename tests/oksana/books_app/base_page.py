from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from .constants import HOST, LOGIN, PASSWORD


class BasePage:
    URL = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(HOST + self.URL)
        return self

    def header(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".main-header").text

    def load(self):
        Wait(self.driver, 5).until(EC.url_contains(self.URL))
        return self


class LoginPage(BasePage):
    URL = "/login"
    HEADER = "Login"

    def login(self):
        login = self.driver.find_element(By.ID, "userName")
        password = self.driver.find_element(By.ID, "password")
        login.send_keys(LOGIN)
        password.send_keys(PASSWORD)
        self.driver.find_element(By.ID, "login").click()
        return ProfilePage(self.driver).load()


class BooksPage(BasePage):
    URL = "/books"

    def get_all_books(self):
        return self.driver.find_elements(By.XPATH, "//img/ancestor::div[contains(@class, 'rt-tr-group')]")

    def go_to_book(self):
        pass


class ProfilePage(BooksPage):
    URL = "/profile"
    HEADER = "Profile"

    def search(self, text):
        self.driver.find_element(By.ID, "searchBox").send_keys(text)
        return self

    def logout(self):
        self.driver.find_element(By.ID, "submit").click()
        return LoginPage(self.driver).load()

    def go_to_book_store(self):
        self.driver.find_element(By.ID, "gotoStore").click()
        return BooksPage(self.driver)
