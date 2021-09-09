from selenium.webdriver.remote.webdriver import WebDriver, By


def test_simple_form(session: WebDriver):

    session.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

    input_field = session.find_element(By.ID, "user-message")
    input_field.send_keys("Hi there")

    form_btn = session.find_element(By.CSS_SELECTOR, "form#get-input button")
    form_btn.click()

    output_text = session.find_element(By.ID, "display")
    assert "Hi there" in output_text.text
