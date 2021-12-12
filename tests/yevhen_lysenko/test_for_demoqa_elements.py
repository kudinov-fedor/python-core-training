from selenium.webdriver.common.by import By


def test_elements_block(driver):
    driver.find_element(By.ID, 'item-0').click()
    driver.find_element(By.ID, 'userName').send_keys('Test message')
    driver.find_element(By.ID, 'submit').click()
    final_text = driver.find_element(By.ID, 'name').text
    assert 'Test message' in final_text
