from selenium.webdriver.common.by import By
from tests.ybilyn.constants import HOST


def test_text_box_page(driver):
    driver.get(HOST + '/text-box')
    full_name_value = 'Adam Smith'
    email_value = 'smith@gmail.com'
    current_address_value = 'Some address, current'
    permanent_address_value = 'Some address, permanent'

    full_name = driver.find_element(By.ID, 'userName')
    email = driver.find_element(By.ID, 'userEmail')
    current_address = driver.find_element(By.XPATH, '//*[@id="currentAddress"]')
    permanent_address = driver.find_element(By.XPATH, '//*[@id="permanentAddress"]')
    submit_button = driver.find_element(By.XPATH, '//*[@id="submit"]')

    full_name.send_keys(full_name_value)
    email.send_keys(email_value)
    current_address.send_keys(current_address_value)
    permanent_address.send_keys(permanent_address_value)

    driver.execute_script("window.scrollBy(0,500)", "")
    submit_button.click()

    assert driver.find_element(By.XPATH, '//*[@id="name"]').text == f'Name:{full_name_value}'
    assert driver.find_element(By.XPATH, '//*[@id="email"]').text == f'Email:{email_value}'
    assert driver.find_element(By.XPATH,
                               '//p[@id="currentAddress"]').text == f'Current Address :{current_address_value}'
    assert driver.find_element(By.XPATH,
                               '//p[@id="permanentAddress"]').text == f'Permananet Address :{permanent_address_value}'
