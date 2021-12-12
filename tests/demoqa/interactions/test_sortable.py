from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def test_sortable(host: str, session: WebDriver):

    session.get(host + "/sortable")

    items = session.find_elements_by_css_selector("#demo-tabpane-list .list-group-item")
    expected = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
    assert [i.text for i in items] == expected

    AC(session).drag_and_drop(items[1], items[4]).perform()

    items = session.find_elements_by_css_selector("#demo-tabpane-list .list-group-item")
    expected = ['One', 'Three', 'Four', 'Five', 'Two', 'Six']
    assert [i.text for i in items] == expected
