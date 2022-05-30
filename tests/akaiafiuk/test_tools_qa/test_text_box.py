from selenium.webdriver.common.by import By
from python_at_2021.tests.akaiafiuk.test_tools_qa.utils import scroll_down

HOST = 'https://demoqa.com'

FULL_NAME_TEXTBOX_LOCATOR = By.ID, 'userName'
EMAIL_TEXTBOX_LOCATOR = By.CSS_SELECTOR, '[type="email"]'
CURRENT_ADDRESS_TEXTBOX_LOCATOR = By.XPATH, './/textarea[@class="form-control"]'
SUBMIT_BTN_LOCATOR = By.CSS_SELECTOR, '[id="submit"]'
FULL_NAME_LABEL_LOCATOR = By.ID, "name"
EMAIL_LABEL_LOCATOR = By.CSS_SELECTOR, '[id="email"]'
CURRENT_ADDRESS_LABEL_LOCATOR = By.XPATH, './/p[@id="currentAddress"]'


def test_text_box(session):
    """Enter data in text boxes and verify that labels with entered data are displayed"""

    # Arrange
    session.get(HOST + '/text-box')
    full_name_textbox = session.find_element(*FULL_NAME_TEXTBOX_LOCATOR)
    email_textbox = session.find_element(*EMAIL_TEXTBOX_LOCATOR)
    current_address_textbox = session.find_element(*CURRENT_ADDRESS_TEXTBOX_LOCATOR)

    # Act
    full_name_textbox.send_keys('John Doe')
    email_textbox.send_keys('jd@gmail.com')
    current_address_textbox.send_keys('New York')
    submit_button = session.find_element(*SUBMIT_BTN_LOCATOR)
    scroll_down(session)
    submit_button.click()
    full_name_label = session.find_element(*FULL_NAME_LABEL_LOCATOR)
    email_label = session.find_element(*EMAIL_LABEL_LOCATOR)
    current_address_label = session.find_element(*CURRENT_ADDRESS_LABEL_LOCATOR)

    # Assert
    assert 'John Doe' in full_name_label.text
    assert 'jd@gmail.com' in email_label.text
    assert 'New York' in current_address_label.text
