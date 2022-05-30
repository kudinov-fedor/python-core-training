from selenium.webdriver.remote.webdriver import WebDriver


def scroll_down(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def forced_click_element(driver, element) -> None:
    driver.execute_script('arguments[0].click();', element)
