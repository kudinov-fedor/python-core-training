import pytest
from appium import webdriver


@pytest.fixture
def driver():
    # set up appium
    desired_caps = dict()
    desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    driver = webdriver.Remote(
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
