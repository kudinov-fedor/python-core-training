from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


WEBSITE = "https://demoqa.com/dragabble"


def test_drag_drop_simple(driver):
    """
    Open website with default tab Simple,
    Drag the object to x=100, y=100
    """
    driver.get(WEBSITE)
    source = driver.find_element(By.ID, "dragBox")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(source, 100, 100).perform()
    assert source.get_attribute("style") == "position: relative; left: 100px; top: 100px;"


def test_drag_and_drop_restricted(driver):
    """
    Open website,
    Click on tab Axis Restricted,
    Drag the object 'Only X' to x=50, y=50,
    Drag the object 'Only Y' to x=50, y=50,
    Verify that 'Only X' moved to x=50, y=0 and 'Only Y' moved to x=0, y=50
    """
    driver.get(WEBSITE)
    driver.find_element(By.XPATH, "//*[@data-rb-event-key='axisRestriction']").click()
    source_x = driver.find_element(By.ID, "restrictedX")
    source_y = driver.find_element(By.ID, "restrictedY")
    action = ActionChains(driver)
    action.click_and_hold(source_x).move_by_offset(50, 50).release().perform()
    action.click_and_hold(source_y).move_by_offset(50, 50).release().perform()
    assert source_x.get_attribute("style") == "position: relative; left: 50px; top: 0px;"
    assert source_y.get_attribute("style") == "position: relative; left: 0px; top: 50px;"


def test_container_restricted(driver):
    """
    Open website,
    Click on tab Container Restricted,
    Try dragging and dropping the object 'I'm contained within the box' to x=-100, y=-100,
    Verify that 'I'm contained within the box' is not possible to move out of the box.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "draggableExample-tab-containerRestriction").click()
    source1 = driver.find_element(By.XPATH, "//*[@id='containmentWrapper']/*[contains(@class, 'draggable')]")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(source1, -100, -100).perform()
    assert source1.get_attribute("style") == "position: relative; left: 0px; top: 0px;"


def test_container_restricted_parent(driver):
    """
    Open website,
    Click on tab Container Restricted,
    Try dragging and dropping the object 'I'm contained within my parent' to x=-100, y=-100,
    Verify that 'I'm contained within my parent' is not possible to move out of the parent element.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "draggableExample-tab-containerRestriction").click()
    source1 = driver.find_element(By.XPATH, "//*[contains(@class, 'ui-widget-header')]")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(source1, -100, -100).perform()
    assert source1.get_attribute("style") == "position: relative;"


def test_cursor_style_center(driver):
    """
    Open website,
    Click on tab Cursor Style,
    Click and hold 'I will always stick to the center',
    Verify that cursor style is 'move'.
    """
    driver.get(WEBSITE)
    driver.find_element(By.ID, "draggableExample-tab-cursorStyle").click()
    source1 = driver.find_element(By.ID, "cursorCenter")
    action = ActionChains(driver)
    action.click_and_hold(source1).perform()
    assert source1.value_of_css_property("cursor") == "move"
