from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests

WEBSITE = "https://demoqa.com/"


def test_opening_new_tab_from_link(driver):
    driver.get(WEBSITE + "links")
    first_tab_handle = driver.window_handles
    link = driver.find_element(By.ID, "simpleLink")
    link.click()
    WebDriverWait(driver, timeout=5).until(
        lambda driver: len(first_tab_handle) != len(driver.window_handles))
    new_tab_handle = driver.window_handles[1]
    driver.switch_to.window(new_tab_handle)
    assert driver.current_url == WEBSITE


def test_link_status(driver):
    driver.get(WEBSITE + "links")
    link = driver.find_element(By.ID, "created")
    link.click()
    for entry in driver.get_log('browser'):
        print(entry)
    assert 0 == 1




