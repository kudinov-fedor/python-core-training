from selenium.webdriver.remote.webdriver import WebDriver


def test_nested_frames(host: str, session: WebDriver):

    session.get(host + "/nestedframes")

    session.switch_to.frame("frame1")
    body = session.find_element_by_css_selector("body")
    assert body.text == "Parent frame"

    nested_frame = session.find_element_by_css_selector("iframe")
    session.switch_to.frame(nested_frame)
    body = session.find_element_by_css_selector("body")
    assert body.text == "Child Iframe"
