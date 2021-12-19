from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

DATA_PICKER_SITE = 'https://demoqa.com/date-picker'


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


def test_buttons(main_page, driver):
    driver.find_element(By.ID, 'item-4').click()
    # identifying the source element
    double_click_button = driver.find_element(By.ID, 'doubleClickBtn')
    # action chain object creation
    action = ActionChains(driver)
    # double click operation and then perform
    action.double_click(double_click_button).perform()
    # read double click message
    double_click_message =\
        driver.find_element(By.ID, 'doubleClickMessage').text
    right_click_button = driver.find_element(By.ID, 'rightClickBtn')
    # right click operation and then perform
    action.context_click(right_click_button).perform()
    # read right click message
    right_click_message = driver.find_element(By.ID, 'rightClickMessage').text
    # click operation and then perform
    click = driver.find_element(By.CSS_SELECTOR,
                                'div>div:nth-child(3)>[type="button"]')
    action.click(on_element=click).perform()
    # read click message
    click_me_message = driver.find_element(By.ID, 'dynamicClickMessage').text
    assert double_click_message == 'You have done a double click'
    assert right_click_message == 'You have done a right click'
    assert click_me_message == 'You have done a dynamic click'


def test_date_picker_1(driver):
    driver.get(DATA_PICKER_SITE)
    picker = driver.find_element(By.ID,
                                 'datePickerMonthYearInput')
    picker.click()
    select_month = Select(driver.find_element(
        By.CLASS_NAME, 'react-datepicker__month-select'))
    select_month.select_by_visible_text('September')
    select_year = Select(driver.find_element(
        By.CLASS_NAME, 'react-datepicker__year-select'))
    select_year.select_by_visible_text('2015')
    selected_day = driver.find_element(
        By.XPATH,
        '//*[contains(@class,"react-datepicker__day'
        ' react-datepicker__day--016")]')
    selected_day.click()
    assert picker.get_attribute("value") == '09/16/2015'


def test_date_picker_2(driver):
    driver.get(DATA_PICKER_SITE)
    picker = driver.find_element(
        By.ID, 'dateAndTimePickerInput')
    picker.click()
    driver.find_element(
        By.XPATH,
        "//*[contains(@class,"
        "'react-datepicker__month-dropdown-container')]").click()
    driver.find_element(By.XPATH,
                        "//*[contains(@class,'react-datepicker__month-option')"
                        " and text() = 'February']").click()
    driver.find_element(By.CLASS_NAME,
                        "react-datepicker__year-read-view--down-arrow").click()
    driver.find_element(By.XPATH,
                        '//*[contains(@class,"react-datepicker__year-option")'
                        'and text() = "2022"]').click()
    driver.find_element(
        By.CSS_SELECTOR,
        ".react-datepicker__day.react-datepicker__day--019").click()
    driver.find_element(By.XPATH,
                        "//*[contains(@class,"
                        "'react-datepicker__time-list-item')"
                        "and text() = '06:45']").click()
    assert picker.get_attribute('value') == 'February 19, 2022 6:45 AM'


def test_progress_bar(driver):
    driver.get('https://demoqa.com/progress-bar')
    driver.find_element(By.ID, 'startStopButton').click()
    driver.find_element(By.CSS_SELECTOR, "[role='progressbar']")
    wait = Wait(driver, 100)
    wait.until(EC.presence_of_element_located((By.ID, 'resetButton')))
    progr_vol = driver.find_element(
        By.XPATH, "//*[contains(@class,"
                  "'progress-bar bg-success')and text() = '100%']")
    assert progr_vol.get_attribute('aria-valuenow') == '100'
