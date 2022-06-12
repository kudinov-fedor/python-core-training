from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def get_element(method):
    def wrapper(self, locator, *args, **kwargs):
        element = self.driver.find_element(*locator)
        return method(self, element, *args, **kwargs)
    return wrapper


def get_element_by_parent(method):
    def wrapper(self, parent, locator, *args, **kwargs):
        element = parent.find_element(*locator)
        return method(self, element, *args, **kwargs)
    return wrapper


def get_selector(method):
    def wrapper(self, locator, *args, **kwargs):
        selector = Select(self.driver.find_element(*locator))
        return method(self, selector, *args, **kwargs)
    return wrapper


def get_elements(method):
    def wrapper(self, locator, *args, **kwargs):
        elements = self.driver.find_elements(*locator)
        return method(self, elements, *args, **kwargs)
    return wrapper


class BasePage():
    BASE_URL = 'https://demoqa.com/'

    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self, page_path=None):
        self.driver.get(f'{self.BASE_URL}{page_path}')
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    def format_xpath_locator(self, xpath, value_to_format):
        return (By.XPATH, xpath.format(value_to_format))

    @get_element
    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)
    
    @get_element
    def confirm_by_enter(self, element):
        element.send_keys(Keys.ENTER)

    @get_element
    def get_text(self, element):
        return element.text
    
    @get_element_by_parent
    def get_text_by_parent(self, element):
        return element.text

    @get_element
    def get_attr(self, element, attribute):
        return element.get_attribute(attribute)
    
    @get_selector
    def select_by_value(self, selector, value):
        selector.select_by_value(str(value))
    
    @get_element
    def is_enabled(self, element):
        return element.is_enabled()
    
    @get_elements
    def get_elements_length(self, elements):
        return len(elements)
    
    @get_elements
    def get_elements_list(self, elements):
        return elements
    
    

