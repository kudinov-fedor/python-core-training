from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_resizable(host: str, session: WebDriver):

    session.get(host + "/resizable")
    box = session.find_element_by_css_selector("#resizableBoxWithRestriction")
    assert box.size == {'height': 200, 'width': 200}

    # different parameters of item
    print(box.location)                           # {'x': 318, 'y': 237}
    print(box.size)                               # {'height': 200, 'width': 200}
    print(box.get_attribute("style"))             # "width: 200px; height: 200px;"
    print(box.get_property("style"))              # ['width', 'height']
    print(box.value_of_css_property("width"))     # "200px"
    print(box.value_of_css_property("height"))    # "200px"

    handler = box.find_element_by_css_selector("span.react-resizable-handle")
    AC(session).click_and_hold(handler).move_by_offset(-50, -100).release().perform()
    assert box.size == {'height': 150, 'width': 150}

    handler = box.find_element_by_css_selector("span.react-resizable-handle")
    AC(session).click_and_hold(handler).move_by_offset(350, 200).release().perform()
    assert box.size == {'height': 300, 'width': 500}
