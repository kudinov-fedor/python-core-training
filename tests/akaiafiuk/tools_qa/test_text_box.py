from selenium.webdriver.common.by import By

HOST = 'https://demoqa.com'

FULL_NAME_TEXTBOX_LOCATOR = (By.ID, 'userName')
EMAIL_TEXTBOX_LOCATOR = (By.CSS_SELECTOR, '[type="email"]')
CURRENT_ADDRESS_TEXTBOX_LOCATOR = (By.XPATH, './/textarea[@class="form-control"]')
SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '[id="submit"]')
FULL_NAME_LABEL_LOCATOR = (By.ID, "name")
EMAIL_LABEL_LOCATOR = (By.CSS_SELECTOR, '[id="email"]')
CURRENT_ADDRESS_LABEL_LOCATOR = (By.XPATH, './/p[@id="currentAddress"]')


def test_text_box(akaiafiuk_session):
    """Enter data in text boxes and verify that labels with entered data are displayed"""

    # Arrange
    akaiafiuk_session.get(HOST + '/text-box')
    full_name_textbox = akaiafiuk_session.find_element(*FULL_NAME_TEXTBOX_LOCATOR)
    email_textbox = akaiafiuk_session.find_element(*EMAIL_TEXTBOX_LOCATOR)
    current_address_textbox = akaiafiuk_session.find_element(*CURRENT_ADDRESS_TEXTBOX_LOCATOR)

    # Act
    full_name_textbox.send_keys('John Doe')
    email_textbox.send_keys('jd@gmail.com')
    current_address_textbox.send_keys('New York')
    submit_button = akaiafiuk_session.find_element(*SUBMIT_BTN_LOCATOR)
    akaiafiuk_session.execute_script('arguments[0].click();', submit_button)
    full_name_label = akaiafiuk_session.find_element(*FULL_NAME_LABEL_LOCATOR)
    email_label = akaiafiuk_session.find_element(*EMAIL_LABEL_LOCATOR)
    current_address_label = akaiafiuk_session.find_element(*CURRENT_ADDRESS_LABEL_LOCATOR)

    # Assert
    assert 'John Doe' in full_name_label.text
    assert 'jd@gmail.com' in email_label.text
    assert 'New York' in current_address_label.text
