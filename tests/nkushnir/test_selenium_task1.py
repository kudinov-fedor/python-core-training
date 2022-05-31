import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac


@pytest.fixture(scope="function")
def driver():
    capabilities = {'browserName': 'firefox', 'marionette': True}
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()

def test_click_buttons(driver):
    driver.get('https://demoqa.com/buttons')
    driver.maximize_window()

    double_click_btn_id = 'doubleClickBtn'
    right_click_btn_id = 'rightClickBtn'
    click_btn_xpath = '//button[contains(@class, "btn-primary") and text()="Click Me"]'
    simple_click_result_id = 'dynamicClickMessage'
    double_click_result_id = 'doubleClickMessage'
    right_click_result_id = 'rightClickMessage'

    simple_click_btn = driver.find_element(By.XPATH, click_btn_xpath)
    driver.execute_script("arguments[0].click()", simple_click_btn)
    right_click_btn = driver.find_element(By.ID, right_click_btn_id)
    ac(driver).context_click(right_click_btn).perform()
    double_click_btn = driver.find_element(By.ID, double_click_btn_id)
    ac(driver).move_to_element(double_click_btn).double_click().perform()

    simple_cilck_result = driver.find_element(By.ID, simple_click_result_id)
    double_click_result = driver.find_element(By.ID, double_click_result_id)
    right_click_result = driver.find_element(By.ID, right_click_result_id)

    assert simple_cilck_result.text == "You have done a dynamic click"
    assert double_click_result.text == "You have done a double click"
    assert right_click_result.text == "You have done a right click"
