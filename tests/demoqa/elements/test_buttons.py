from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_checkbox(host: str, session: WebDriver):

    session.get(host + "/buttons")
    doubleClickBtn = session.find_element_by_css_selector("#doubleClickBtn")
    rightClickBtn = session.find_element_by_css_selector("#rightClickBtn")
    clickBtn = session.find_element_by_xpath("//button[text()='Click Me']")

    AC(session).double_click(doubleClickBtn).perform()
    doubleClickMessage = session.find_element_by_css_selector("#doubleClickMessage")
    assert doubleClickMessage.text == "You have done a double click"

    AC(session).context_click(rightClickBtn).perform()
    rightClickMessage = session.find_element_by_css_selector("#rightClickMessage")
    assert rightClickMessage.text == "You have done a right click"

    clickBtn.click()
    dynamicClickMessage = session.find_element_by_css_selector("#dynamicClickMessage")
    assert dynamicClickMessage.text == "You have done a dynamic click"
