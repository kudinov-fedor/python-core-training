from selenium.webdriver.common.by import By


class LoginPageElements:
    def __init__(self):
        self.login_page_header = (By.CSS_SELECTOR, ".main-header")
        self.username_field = (By.CSS_SELECTOR, '#userName-wrapper #userName')
        self.password_field = (By.CSS_SELECTOR, 'password-wrapper #password')
        self.login_button = (By.CSS_SELECTOR, 'button#login')
        self.new_user_button = (By.CSS_SELECTOR, 'button#newUser')
        self.error_massage = (By.CSS_SELECTOR, '#output #name')
