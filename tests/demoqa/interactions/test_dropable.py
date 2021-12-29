from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_droppable(host: str, session: WebDriver):

    session.get(host + "/droppable")

    draggable = session.find_element_by_css_selector("#draggable")
    droppable = session.find_element_by_css_selector("#droppable")
    assert droppable.text == "Drop here"

    AC(session).drag_and_drop(draggable, droppable).perform()
    assert droppable.text == "Dropped!"
