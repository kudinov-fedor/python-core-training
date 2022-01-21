from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest


WEBSITE = "https://demoqa.com/tool-tips"


@pytest.mark.parametrize("element_xpath, expected_text", [
    ("//*[@id='toolTipButton']", "You hovered over the Button"),
    ("//*[@id='toolTipTextField']", "You hovered over the text field"),
    ("//*[@id='texToolTopContainer']//a[1]", "You hovered over the Contrary")
])
def test_button_tooltip(driver, element_xpath, expected_text):
    """
    Check tooltip of a button, a text field and a link.
    """
    driver.get(WEBSITE)
    tooltipButton = driver.find_element(By.XPATH, element_xpath)
    action = ActionChains(driver)
    action.move_to_element(tooltipButton).perform()
    tooltip = driver.find_element(By.XPATH, "//div[@class='tooltip-inner']")
    assert tooltip.text == expected_text
