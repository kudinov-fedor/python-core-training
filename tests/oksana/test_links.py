from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pytest
from urllib.parse import urljoin

WEBSITE = "https://demoqa.com/"


def test_opening_new_tab_from_link(driver):
    """
    Click on link and check that a new tab is open with the home page.
    """
    driver.get(WEBSITE + "links")
    link = driver.find_element(By.ID, "simpleLink")
    link.click()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    new_tab_handle = driver.window_handles[-1]  # latest opened window
    driver.switch_to.window(new_tab_handle)
    assert driver.current_url == WEBSITE


@pytest.mark.parametrize("text, status_code", [
    ("Created", 201),
    ("No Content", 204),
    ("Bad Request", 400)
])
def test_link_status_response(driver, text, status_code):
    """
    Click on the link and check the response of the request.
    """
    driver.get(WEBSITE + "links")
    link = driver.find_element(By.XPATH, "//a[text()='{}']".format(text))
    path = link.get_attribute("id")
    link.click()
    res = requests.head(urljoin(WEBSITE, path))
    assert res.status_code == status_code
