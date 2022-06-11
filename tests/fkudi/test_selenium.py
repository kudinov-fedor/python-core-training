import os
import time
import pytest

from selenium.webdriver import Chrome, Firefox, Edge, Opera, Safari

from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver_path = os.environ.get("DRIVER_PATH", "chromedriver")
HOST = "https://demoqa.com"


def scroll_down_page(session: WebDriver):
    session.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def test_some(session):
    session.get(HOST + "/books")

    TABLE_ROW = By.XPATH, "//div[contains(@class, 'books-wrapper')]" \
                          "//img/ancestor::div[contains(@class, 'rt-tr-group')]"
    BOOK_TITLE = By.XPATH, './/a'
    BOOK_AUTHOR = By.XPATH, ".//div[contains(@class, 'rt-td')][3]"

    row = session.find_elements(*TABLE_ROW)[2]  # get 3rd row
    title = row.find_element(*BOOK_TITLE)
    author = row.find_element(*BOOK_AUTHOR)

    assert title.text == 'Designing Evolvable Web APIs with ASP.NET'
    assert author.text == 'Glenn Block et al.'


def test_ajax(session: WebDriver):

    session.get("https://demoqa.com/profile")

    btn = session.find_element(By.CSS_SELECTOR, "#demo button")
    btn.click()

    text = Wait(session, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#demo h1")))
    # text = session.find_element(By.CSS_SELECTOR, "#demo h1")

    assert text.text == "AJAX"


def test_simple_input_field(session):
    session.get(HOST + "/text-box")

    field = session.find_element(By.ID, "userName")
    field.send_keys("test")

    scroll_down_page(session)  # scroll down as add covers button

    submit = session.find_element(By.CSS_SELECTOR, "button#submit")
    submit.click()

    result_field = session.find_element(By.XPATH, "//p[@id='name']")
    assert result_field.text == "Name:test"
