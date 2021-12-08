from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_checkbox(host: str, session: WebDriver):

    session.get(host + "/radio-button")
    yesRadio = session.find_element_by_css_selector("#yesRadio")
    impressiveRadio = session.find_element_by_css_selector("#impressiveRadio")
    noRadio = session.find_element_by_css_selector("#noRadio")

    # yesRadio.click()  # error Other element will receive click
    AC(session).click(yesRadio).perform()  # click on location
    textSuccess = session.find_element_by_css_selector(".text-success")
    assert textSuccess.text == "Yes"

    AC(session).click(noRadio).perform()
    assert textSuccess.text == "Yes"

    AC(session).click(impressiveRadio).perform()
    assert textSuccess.text == "Impressive"
