from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def scroll_down(driver: WebDriver) -> None:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def forced_click_element(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script('arguments[0].click();', element)
