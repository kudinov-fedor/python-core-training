from datetime import date
from selenium.webdriver.remote.webdriver import WebDriver

from .helpers import DatePickerBootstrap


def test_date_picker(session: WebDriver):
    """
    Future Dates Disabled
    Days Of Week Disabled- Sunday
    Week Starts from Monday
    Click on 'Today' to select Current date
    Click on Clear button to clear the date entered
    """

    # todo how test will work on Sunday?
    session.get("https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html")
    dp = DatePickerBootstrap(session)
    dp.click()
    dp.today()
    assert dp.get_value() == date.today().strftime("%d/%m/%Y")
