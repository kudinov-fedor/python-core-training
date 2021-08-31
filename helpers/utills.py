from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException,
                                        ElementNotSelectableException,
                                        InvalidElementStateException)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command


# monkey patch the find_by_css_selector method :
# def webdriver_s(self, value):
#     return self.execute(Command.FIND_ELEMENT, {
#         'using': "css selector",  # By.CSS_SELECTOR,
#         'value': value})['value']
#
#
# def webdriver_ss(self, value):
#     return self.execute(Command.FIND_ELEMENTS, {
#         'using': "css selector",  # By.CSS_SELECTOR,
#         'value': value})['value']
#
#
# def webelement_s(self, value):
#     return self._execute(Command.FIND_ELEMENT, {
#         'using': "css selector",  # By.CSS_SELECTOR,
#         'value': value})['value']
#
#
# def webelement_ss(self, value):
#     return self._execute(Command.FIND_ELEMENTS, {
#         'using': "css selector",  # By.CSS_SELECTOR,
#         'value': value})['value']


# WebDriver.s = webdriver_s
# WebDriver.ss = webdriver_ss
# WebElement.s = webelement_s
# WebElement.ss = webelement_ss


def open_tab(web_driver: WebDriver, tab):
    web_driver.switch_to.window(web_driver.window_handles[tab])


def wait_element(web_driver: WebDriver, css_selector):
    WebDriverWait(web_driver, 10).until(lambda driver: driver.find_element_by_css_selector(css_selector).is_displayed())
    return web_driver.find_element_by_css_selector(css_selector)


def wait_title(web_driver, title):
    WebDriverWait(web_driver, 10).until(lambda driver: title in driver.title)


def page_loaded(web_driver):
    page_state = web_driver.execute_script('return document.readyState;')
    return page_state == 'complete'


def wait_page_loaded(web_driver):
    WebDriverWait(web_driver, 10).until(lambda driver: page_loaded(driver))


def execute_script(web_driver, script_name=None, css="", value=""):
    scripts = {
        "send_keys": "$('{css}').val('{value}')".format(css=css, value=value),
        "click": '$("{css}").click();'.format(css=css),
        "scroll_to_bottom": "document.body.scrollTop = document.body.scrollHeight;"
    }
    script = scripts[script_name]
    web_driver.execute_script(script)
