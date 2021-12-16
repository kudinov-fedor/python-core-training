from selenium.webdriver.common.by import By


def test_elements_block(main_page, driver):
    driver.find_element(By.ID, 'item-0').click()
    driver.find_element(By.ID, 'userName').send_keys('Test message')
    driver.find_element(By.ID, 'submit').click()
    final_text = driver.find_element(By.ID, 'name').text
    assert 'Test message' in final_text


def test_check_box(main_page, driver):
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


def test_radio_button(main_page, driver):
    driver.find_element(By.ID, 'item-2').click()
    driver.find_element(By.CSS_SELECTOR, '[for="impressiveRadio"]').click()
    yes_response = driver.find_element(By.CLASS_NAME, 'text-success').text
    assert yes_response == 'Impressive'


def test_form(main_page, driver):
    driver.find_element(By.ID, 'item-3').click()
    driver.find_element(By.ID, 'addNewRecordButton').click()
    driver.find_element(By.ID, 'firstName').send_keys('Yevhen')
    driver.find_element(By.ID, 'lastName').send_keys('Lysenko')
    driver.find_element(By.ID, 'userEmail').send_keys('test@mail.com')
    driver.find_element(By.ID, 'age').send_keys('34')
    driver.find_element(By.ID, 'salary').send_keys('7000')
    driver.find_element(By.ID, 'department').send_keys('IT Security')
    driver.find_element(By.ID, 'submit').click()
    items_list = []
    for element in driver.find_elements(By.CLASS_NAME, 'rt-td'):
        items_list.append(element.text)
    assert 'Yevhen' in items_list
    assert 'Lysenko' in items_list
    assert 'test@mail.com' in items_list
    assert '34' in items_list
    assert '7000' in items_list
    assert 'IT Security' in items_list




