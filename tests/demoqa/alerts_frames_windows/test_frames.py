from selenium.webdriver.remote.webdriver import WebDriver


def test_frames(host: str, session: WebDriver):

    session.get(host + "/frames")
    mainHeader = session.find_element_by_css_selector(".main-header")
    assert mainHeader.text == "Frames"

    session.switch_to.frame("frame1")
    sampleHeading = session.find_element_by_css_selector("#sampleHeading")
    assert sampleHeading.text == "This is a sample page"

    session.switch_to.parent_frame()
    mainHeader = session.find_element_by_css_selector(".main-header")
    assert mainHeader.text == "Frames"

    session.switch_to.frame("frame2")
    sampleHeading = session.find_element_by_css_selector("#sampleHeading")
    assert sampleHeading.text == "This is a sample page"
