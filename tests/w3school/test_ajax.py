from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.remote.webdriver import By


def test_ajax(host: str, session: WebDriver):

    session.get(host + "/js/js_ajax_intro.asp")

    btn = session.find_element(By.CSS_SELECTOR, "#demo button")
    btn.click()

    text_locator = (By.CSS_SELECTOR, "#demo h1")
    text = Wait(session, 10).until(EC.visibility_of_element_located(text_locator))
    assert text.text == "AJAX"
