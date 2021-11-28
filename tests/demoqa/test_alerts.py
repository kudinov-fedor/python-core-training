from selenium.webdriver.remote.webdriver import WebDriver


def test_prompt_alerts(host: str, session: WebDriver):
    """
    alert_obj.accept() – used to accept the Alert
    alert_obj.dismiss() – used to cancel the Alert
    alert.send_keys() – used to enter a value in the Alert text box.
    alert.text() – used to retrieve the message included in the Alert pop-up.
    """

    session.get(host + "/alerts")
    promtButton = session.find_element_by_css_selector("#promtButton")
    promtButton.click()

    alert = session.switch_to.alert
    alert.send_keys("text sent to alert")
    alert.accept()

    promptResult = session.find_element_by_css_selector("#promptResult")
    assert promptResult.text == "You entered text sent to alert"
