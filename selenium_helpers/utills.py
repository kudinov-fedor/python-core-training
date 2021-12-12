# flake8: noqa

import time
import os

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


def retry(times: int = 1, exceptions=Exception, timeout: int = 0):
    """
    Retry Decorator
    Retries the wrapped function/method `times` times if the exceptions listed
    in ``exceptions`` are thrown
    :param times: The number of times to repeat the wrapped function/method
    :type times: Int
    :param exceptions: Lists of exceptions that trigger a retry attempt
    :type exceptions: Tuple of Exceptions
    :param timeout: Timeout beetween retries
    :type timeout: Int
    """
    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
                    )
                    attempt += 1
                    time.sleep(timeout)
            return func(*args, **kwargs)
        return newfn
    return decorator


# read file with retries
@retry(5, FileNotFoundError, timeout=1)
def read_file(path, **kwargs):
    with open(path, **kwargs) as file:
        return file.read()


# check file is present with retries
@retry(5, AssertionError, timeout=1)
def assert_file_is_present(path, **kwargs):
    assert os.path.exists(path)
