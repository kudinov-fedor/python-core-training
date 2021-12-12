from selenium.webdriver.common.by import By


def test_elements_block(driver):
    driver.find_element(By.ID, 'item-0').click()
    driver.find_element(By.ID, 'userName').send_keys('Test message')
    driver.find_element(By.ID, 'submit').click()
    final_text = driver.find_element(By.ID, 'name').text
    assert 'Test message' in final_text


def test_check_box(driver):
    driver.find_element(By.ID, 'item-1').click()
    element_first = driver.find_element(By.CSS_SELECTOR,
                                        '#tree-node > ol > li'
                                        ' > span > button > svg')
    element_first.click()
    selected_tree = driver.find_element(By.CSS_SELECTOR,
                                        '#tree-node > ol > li'
                                        ' > span > label > span.rct-title')
    selected_tree.click()
    displayed_result = driver.find_element(By.ID, 'result')
    assert 'home' in displayed_result.text
