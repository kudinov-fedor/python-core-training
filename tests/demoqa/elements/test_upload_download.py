import os

from selenium.webdriver.remote.webdriver import WebDriver

from selenium_helpers.utills import assert_file_is_present


def test_download(host: str, session: WebDriver, tmp_dir):

    session.get(host + "/upload-download")
    downloadButton = session.find_element_by_id("downloadButton")
    file_name = downloadButton.get_attribute("download")

    downloadButton.click()
    assert_file_is_present(os.path.join(tmp_dir, file_name))


def test_upload(host: str, session: WebDriver):

    session.get(host + "/upload-download")
    uploadFile = session.find_element_by_id("uploadFile")

    sample_file = os.path.join(os.path.dirname(__file__), "sample_data", "sample_data.txt")
    uploadFile.send_keys(sample_file)
    assert session.find_element_by_id("uploadedFilePath").text == r"C:\fakepath\sample_data.txt"
