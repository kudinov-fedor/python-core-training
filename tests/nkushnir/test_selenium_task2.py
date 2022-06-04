from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

WINDOWS_DEMO_URL = 'https://demoqa.com/browser-windows'


def test_switch_to_new_tab(driver):
    TAB_BUTTON_ID = (By.ID, 'tabButton')
    NEW_WINDOW_TEXT_ID = (By.ID, 'sampleHeading')

    driver.get(WINDOWS_DEMO_URL)
    driver.find_element(*TAB_BUTTON_ID).click()
    Wait(driver, 5).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    new_window = driver.current_window_handle
    new_window_text = driver.find_element(*NEW_WINDOW_TEXT_ID).text

    assert new_window == windows[1], 'User is not switched to new window'
    assert new_window_text == 'This is a sample page', 'Text is different from expected'


def test_close_new_window(driver):
    NEW_WINDOW_MESSAGE_ID = (By.ID, 'messageWindowButton')
    MESSAGE_BODY = (By.XPATH, '//body')

    driver.get(WINDOWS_DEMO_URL)
    driver.find_element(*NEW_WINDOW_MESSAGE_ID).click()
    Wait(driver, 5).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    message_text = driver.find_element(*MESSAGE_BODY).text
    driver.close()
    current_windows = driver.window_handles

    assert message_text == (
        'Knowledge increases by sharing but not by saving. '
        'Please share this website with your friends and in your organization.'
        ), 'New window text is diferent from expected'
    assert len(current_windows) == 1, 'New message window is not closed'