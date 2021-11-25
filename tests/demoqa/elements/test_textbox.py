from selenium.webdriver.remote.webdriver import WebDriver


def test_text_box(host: str, session: WebDriver):

    session.get(host + "/text-box")

    userName = session.find_element_by_css_selector("input#userName")
    userEmail = session.find_element_by_css_selector("input#userEmail")
    currentAddress = session.find_element_by_css_selector("textarea#currentAddress")
    permanentAddress = session.find_element_by_css_selector("textarea#permanentAddress")
    submit_btn = session.find_element_by_css_selector("button#submit")

    userName.send_keys("A")
    userEmail.send_keys("b@b.com")
    currentAddress.send_keys("C")
    permanentAddress.send_keys("D")
    submit_btn.click()

    # check
    userName = session.find_element_by_css_selector("p#name")
    userEmail = session.find_element_by_css_selector("p#email")
    currentAddress = session.find_element_by_css_selector("p#currentAddress")
    permanentAddress = session.find_element_by_css_selector("p#permanentAddress")

    assert "A" in userName.text
    assert "b@b.com" in userEmail.text
    assert "C" in currentAddress.text
    assert "D" in permanentAddress.text
