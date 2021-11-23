from selenium.webdriver.remote.webdriver import WebDriver


def test_date_range_picker(session: WebDriver):
    """
    Days Of Week Disabled- Sunday
    Week Starts from Sunday
    Selected Date will be displayed in both fields. Ex: Selected Start date will be pre-populated in end date
    Start date should be less than end date
    """
    session.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
