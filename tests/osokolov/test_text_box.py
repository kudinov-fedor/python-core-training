from selenium.webdriver.common.by import By

HOST = 'https://demoqa.com'


def test_text_box(browser):
    path = '/text-box'
    browser.get(f'{HOST}{path}')

    name = 'Test name'
    email = 'test@mail.com'
    address = 'Test address'

    name_field = browser.find_element(By.CSS_SELECTOR, '#userName')
    email_field = browser.find_element(By.CSS_SELECTOR, '#userEmail')
    current_address_field = browser.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button#submit')

    name_field.send_keys(name)
    email_field.send_keys(email)
    current_address_field.send_keys(address)

    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    name_result = browser.find_element(By.XPATH, '//div[@id="output"]//p[@id="name"]')
    email_result = browser.find_element(By.XPATH, '//div[@id="output"]//p[@id="email"]')
    current_address_result = browser.find_element(By.XPATH, '//div[@id="output"]//p[@id="currentAddress"]')

    assert name_result.text == f'Name:{name}'
    assert email_result.text == f'Email:{email}'
    assert current_address_result.text == f'Current Address :{address}'
