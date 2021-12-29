from selenium.webdriver.remote.webdriver import WebDriver


def test_checkbox(host: str, session: WebDriver):

    session.get(host + "/checkbox")
    home = session.find_element_by_css_selector("label[for='tree-node-home']")
    home.click()

    items = session.find_elements_by_css_selector("#result .text-success")
    expected = ["home", "desktop", "notes", "commands", "documents", "workspace",
                "react", "angular", "veu", "office", "public", "private", "classified",
                "general", "downloads", "wordFile", "excelFile"]
    assert [i.text for i in items] == expected
