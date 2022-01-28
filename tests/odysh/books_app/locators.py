from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_field = By.ID, 'userName'
    pwd_name_field = By.ID, 'password'
    login_btn = By.ID, 'login'


class ProfilePageLocators:
    user_name_value = By.ID, 'userName-value'


class BooksPageLocators:
    search_book_field = By.ID, 'searchBox'
    git_book = By.ID, 'see-book-Git Pocket Guide'
