import pytest
import requests
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.parametrize("text, code", [
    ("Created", 201),
    ("Bad Request", 400),
    ("Not Found", 404),
])
def test_links(host: str, session: WebDriver, text, code):

    session.get(host + "/links")
    element = session.find_element_by_xpath("//a[text()='{}']".format(text))
    path = element.get_attribute("id")
    r = requests.head("{}/{}".format(host, path))
    assert r.status_code == code
