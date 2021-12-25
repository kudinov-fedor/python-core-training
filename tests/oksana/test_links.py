from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests

WEBSITE = "https://demoqa.com/"
CREATED_LINK = "created"
NO_CONTENT_LINK = "no-content"
BAD_REQUEST = "bad-request"


def test_opening_new_tab_from_link(driver):
    """
    Click on link and check that a new tab is open with the home page.
    """
    driver.get(WEBSITE + "links")
    first_tab_handle = driver.window_handles
    link = driver.find_element(By.ID, "simpleLink")
    link.click()
    WebDriverWait(driver, timeout=5).until(
        lambda driver: len(first_tab_handle) != len(driver.window_handles))
    new_tab_handle = driver.window_handles[1]
    driver.switch_to.window(new_tab_handle)
    assert driver.current_url == WEBSITE


def test_link_status_created(driver):
    """
    Click on the link and check the response of the request is 201.
    """
    driver.get(WEBSITE + "links")
    link = driver.find_element(By.ID, CREATED_LINK)
    link.click()
    res = requests.head(WEBSITE + CREATED_LINK)
    assert res.status_code == 201


def test_link_status_no_content(driver):
    """
    Click on the link and check the response of the request is 204.
    """
    driver.get(WEBSITE + "links")
    link = driver.find_element(By.ID, NO_CONTENT_LINK)
    link.click()
    res = requests.head(WEBSITE + NO_CONTENT_LINK)
    assert res.status_code == 204


def test_link_status_bad_request(driver):
    """
    Click on the link and check the response of the request is 400.
    """
    driver.get(WEBSITE + "links")
    link = driver.find_element(By.ID, BAD_REQUEST)
    link.click()
    res = requests.head(WEBSITE + BAD_REQUEST)
    assert res.status_code == 400
