import time

from selenium.webdriver.remote.webdriver import WebDriver, By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


SHOW_AND_HIDE_SCRIPT = "{script}  setTimeout(function (){{waitingDialog.hide();}}, {timeout}000);"


def test_simple_dialog(session: WebDriver):

    session.get("https://www.seleniumeasy.com/test/bootstrap-progress-bar-dialog-demo.html")
    simple_script = SHOW_AND_HIDE_SCRIPT.format(script="waitingDialog.show();", timeout=2)
    session.execute_script(simple_script)

    assert WebDriverWait(session, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal.fade.in")))
    time.sleep(1)
    assert session.find_elements(By.CSS_SELECTOR, ".modal.fade.in")
    time.sleep(1)
    assert not session.find_elements(By.CSS_SELECTOR, ".modal.fade.in")
