from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


WEBSITE = "https://demoqa.com/date-picker"


def test_date_selection(driver):
    """
    Open website,
    Click on Select day datepicker,
    Click on month dropdown and select January,
    Click on year dropdown and select 2019,
    Select 1st day of the month,
    Verify "Select day" value equals to "01/01/2019"
    """
    driver.get(WEBSITE)
    date_picker = driver.find_element(By.ID, "datePickerMonthYearInput")
    date_picker.click()
    month = Select(driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__month-select')]"))
    month.select_by_value("0")
    year = Select(driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__year-select')]"))
    year.select_by_value("2019")
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__day react-datepicker__day--001')]").click()
    assert date_picker.get_attribute("value") == "01/01/2019"


def test_date_and_time_selection(driver):
    """
    Open website,
    Click on Date and time datepicker,
    Click on month dropdown and select January,
    Click on year dropdown and select 2019,
    Select 1st day of the month,
    Select 07:00,
    Verify "Date and time" value equals to "January 1, 2019 7:00 AM"
    """
    driver.get(WEBSITE)
    date_picker = driver.find_element(By.ID, "dateAndTimePickerInput")
    date_picker.click()
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__month-dropdown-container')]").click()
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__month-option') and text() = 'January']").click()
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__year-read-view')]").click()
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__year-option') and text() = '2019']").click()
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__day--001')]").click()
    driver.find_element(By.XPATH, "//*[contains(@class,'react-datepicker__time-list-item') and text() = '07:00']").click()
    assert date_picker.get_attribute("value") == "January 1, 2019 7:00 AM"
