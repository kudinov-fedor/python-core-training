from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_tool_tip_btn(host: str, session: WebDriver):

    session.get(host + "/tool-tips")

    toolTipButton = session.find_element_by_css_selector("#toolTipButton")
    AC(session).move_to_element(toolTipButton).perform()
    buttonToolTipLocator = By.ID, "buttonToolTip"
    Wait(session, 5).until(EC.text_to_be_present_in_element(buttonToolTipLocator, "You hovered over the Button"))


def test_tool_tip_input(host: str, session: WebDriver):

    session.get(host + "/tool-tips")

    toolTipTextField = session.find_element_by_css_selector("#toolTipTextField")
    AC(session).move_to_element(toolTipTextField).perform()
    textFieldToolTipLocator = By.ID, "textFieldToolTip"
    Wait(session, 5).until(EC.text_to_be_present_in_element(textFieldToolTipLocator, "You hovered over the text field"))


def test_tool_tip_link(host: str, session: WebDriver):

    session.get(host + "/tool-tips")

    texToolTopContainer = session.find_element_by_css_selector("#texToolTopContainer")
    toolTipLink = texToolTopContainer.find_element_by_xpath("//a[text()='Contrary']")
    AC(session).move_to_element(toolTipLink).perform()
    contraryTexToolTip = By.ID, "contraryTexToolTip"
    Wait(session, 5).until(EC.text_to_be_present_in_element(contraryTexToolTip, "You hovered over the Contrary"))
