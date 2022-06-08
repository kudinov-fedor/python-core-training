from selenium.webdriver.common.by import By
import pytest

HOST = 'https://demoqa.com'


@pytest.fixture(autouse=True)
def setup(browser):
    path = '/radio-button'
    browser.get(f'{HOST}{path}')


class TestRadioButtons:

    def test_yes_button(self, browser):
        yes_button = browser.find_element(By.CSS_SELECTOR, '[for="yesRadio"]')
        yes_button.click()
        text_result = browser.find_element(By.CSS_SELECTOR, '.text-success').text

        assert text_result == 'Yes'

    def test_impressive_button(self, browser):
        impressive_button = browser.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]')
        impressive_button.click()
        text_result = browser.find_element(By.CSS_SELECTOR, '.text-success').text

        assert text_result == 'Impressive'

    def test_no_button(self, browser):
        no_button = browser.find_element(By.CSS_SELECTOR, '#noRadio')

        assert not no_button.is_enabled()
