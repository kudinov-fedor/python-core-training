import pytest
from appium.webdriver import Remote as _Remote


#  https://stackoverflow.com/a/48836462/10754683
class Remote(_Remote):
    def _unwrap_value(self, value):
        if isinstance(value, dict):
            if 'ELEMENT' in value:
                return self.create_web_element(value['ELEMENT'])
            elif 'SHADOW' in value:
                return self._shadowroot_cls(self, value['SHADOW'])
            elif 'element-6066-11e4-a52e-4f735466cecf' in value:
                return self.create_web_element(value['element-6066-11e4-a52e-4f735466cecf'])
            elif 'shadow-6066-11e4-a52e-4f735466cecf' in value:
                return self._shadowroot_cls(self, value['shadow-6066-11e4-a52e-4f735466cecf'])
            else:
                for key, val in value.items():
                    value[key] = self._unwrap_value(val)
                return value
        elif isinstance(value, list):
            return list(self._unwrap_value(item) for item in value)
        else:
            return value


@pytest.fixture
def driver():
    # set up appium
    desired_caps = dict()
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    driver = Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=desired_caps)
    yield driver
    driver.quit()


def getresults(driver):
    displaytext = driver.find_element_by_accessibility_id("CalculatorResults").text
    displaytext = displaytext.strip("Display is ")
    displaytext = displaytext.rstrip(' ')
    displaytext = displaytext.lstrip(' ')
    return displaytext


def test_initialize(driver):
    driver.find_element_by_name("Clear").click()
    driver.find_element_by_name("Seven").click()
    assert getresults(driver) == "7"
    driver.find_element_by_name("Clear").click()


def test_addition(driver):
    driver.find_element_by_name("One").click()
    driver.find_element_by_name("Plus").click()
    driver.find_element_by_name("Seven").click()
    driver.find_element_by_name("Equals").click()
    assert getresults(driver) == "8"


def test_combination(driver):
    driver.find_element_by_name("Seven").click()
    driver.find_element_by_name("Multiply by").click()
    driver.find_element_by_name("Nine").click()
    driver.find_element_by_name("Plus").click()
    driver.find_element_by_name("One").click()
    driver.find_element_by_name("Equals").click()
    driver.find_element_by_name("Divide by").click()
    driver.find_element_by_name("Eight").click()
    driver.find_element_by_name("Equals").click()
    assert getresults(driver) == "8"


def test_division(driver):
    driver.find_element_by_name("Eight").click()
    driver.find_element_by_name("Eight").click()
    driver.find_element_by_name("Divide by").click()
    driver.find_element_by_name("One").click()
    driver.find_element_by_name("One").click()
    driver.find_element_by_name("Equals").click()
    assert getresults(driver) == "8"


def test_multiplication(driver):
    driver.find_element_by_name("Nine").click()
    driver.find_element_by_name("Multiply by").click()
    driver.find_element_by_name("Nine").click()
    driver.find_element_by_name("Equals").click()
    assert getresults(driver) == "81"


def test_subtraction(driver):
    driver.find_element_by_name("Nine").click()
    driver.find_element_by_name("Minus").click()
    driver.find_element_by_name("One").click()
    driver.find_element_by_name("Equals").click()
    assert getresults(driver) == "8"
