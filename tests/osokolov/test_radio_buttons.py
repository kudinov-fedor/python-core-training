from selenium.webdriver.common.by import By
import pytest

HOST = 'https://demoqa.com'


@pytest.fixture(scope="class")
def pre_condition(browser):
    path = '/radio-button'
    browser.implicitly_wait(2)
    browser.get(f'{HOST}{path}')
    return browser


class TestRadioButtons:

    def test_yes_button(self, pre_condition):
        browser = pre_condition
        yes_button = browser.find_element(By.CSS_SELECTOR, '[for="yesRadio"]')
        yes_button.is_enabled().click()
        text_result = browser.find_element(By.CSS_SELECTOR, '.text-success').text

        assert text_result == 'Yes'

    def test_impressive_button(self, pre_condition):
        browser = pre_condition
        impressive_button = browser.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]')
        impressive_button.is_enabled().click()
        text_result = browser.find_element(By.CSS_SELECTOR, '.text-success').text

        assert text_result == 'Impressive'

    def test_no_button(self, pre_condition):
        browser = pre_condition
        no_button = browser.find_element(By.CSS_SELECTOR, '#noRadio')

        assert not no_button.is_enabled()
