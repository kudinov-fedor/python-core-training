from .base_page import LoginPage, ProfilePage


def test_login(driver):
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    login_page.open().login()
    assert profile_page.header() == ProfilePage.HEADER
