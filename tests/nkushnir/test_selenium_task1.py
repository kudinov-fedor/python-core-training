import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac


SELENIUM_HOST = 'http://127.0.0.1'
SELENIUM_PORT = '4444'
BUTTONS_DEMO_URL = 'https://demoqa.com/buttons'

@pytest.fixture(scope="module")
def driver():
    capabilities = {'browserName': 'firefox', 'marionette': True}
    driver = webdriver.Remote(
        command_executor=f'{SELENIUM_HOST}:{SELENIUM_PORT}/wd/hub',
        desired_capabilities=capabilities
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_click_by_js(driver):
    driver.get(BUTTONS_DEMO_URL)
    click_btn_xpath = '//button[contains(@class, "btn-primary") and text()="Click Me"]'
    simple_click_result_id = 'dynamicClickMessage'
    simple_click_btn = driver.find_element(By.XPATH, click_btn_xpath)
    driver.execute_script("arguments[0].click()", simple_click_btn)
    simple_cilck_result = driver.find_element(By.ID, simple_click_result_id)
    assert simple_cilck_result.text == "You have done a dynamic click"

def test_right_click(driver):
    driver.get(BUTTONS_DEMO_URL)
    right_click_btn_id = 'rightClickBtn'
    right_click_result_id = 'rightClickMessage'
    right_click_btn = driver.find_element(By.ID, right_click_btn_id)
    ac(driver).context_click(right_click_btn).perform()
    right_click_result = driver.find_element(By.ID, right_click_result_id)
    assert right_click_result.text == "You have done a right click"

def test_move_and_double_click(driver):
    driver.get(BUTTONS_DEMO_URL)
    double_click_btn_id = 'doubleClickBtn'
    double_click_result_id = 'doubleClickMessage'
    double_click_btn = driver.find_element(By.ID, double_click_btn_id)
    ac(driver).move_to_element(double_click_btn).double_click().perform()
    double_click_result = driver.find_element(By.ID, double_click_result_id)
    assert double_click_result.text == "You have done a double click"
