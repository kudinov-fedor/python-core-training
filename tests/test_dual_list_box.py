from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.keys import Keys


def test_dual_list_box(session: WebDriver):

    session.get("https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html")

    items = session.find_elements(By.CSS_SELECTOR, "select.pickData > option")
    add_btn = session.find_element(By.CSS_SELECTOR, "button.pAdd")

    AC(session).key_down(Keys.LEFT_SHIFT).click(items[1]).click(items[3]).key_up(Keys.LEFT_SHIFT).perform()
    add_btn.click()

    items = session.find_elements(By.CSS_SELECTOR, "select.pickListResult > option")
    assert len(items) == 3
