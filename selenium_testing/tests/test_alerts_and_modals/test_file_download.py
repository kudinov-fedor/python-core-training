import os

from selenium.webdriver.remote.webdriver import WebDriver, By

from selenium_testing.helpers.utills import read_file


VALUE = "abcd\n12345"


def test_download_file(session: WebDriver, tmp_dir):

    session.get("https://www.seleniumeasy.com/test/generate-file-to-download-demo.html")
    session.find_element(By.ID, "textbox").send_keys(VALUE)
    assert session.find_element(By.ID, "textarea_feedback").text == "{} characters remaining".format(500 - len(VALUE))
    session.find_element(By.ID, "create").click()

    session.find_element(By.ID, "link-to-download").click()

    assert read_file(os.path.join(tmp_dir, "easyinfo.txt")) == VALUE

    # check by link
    path = session.find_element(By.ID, "link-to-download").get_property("href")
    session.get(path)
    assert session.find_element(By.CSS_SELECTOR, "body").text == VALUE
