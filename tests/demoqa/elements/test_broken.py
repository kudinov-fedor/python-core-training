import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


@pytest.mark.xfail(reason="Fails due to broken image")
def test_broken(host: str, session: WebDriver):

    session.get(host + "/broken")

    image = session.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa.jpg']")
    size = image.size
    assert size["height"] > 16
    assert size["width"] > 16

    image = session.find_element(By.CSS_SELECTOR, "img[src='/images/Toolsqa_1.jpg']")
    size = image.size
    assert size["height"] > 16
    assert size["width"] > 16
