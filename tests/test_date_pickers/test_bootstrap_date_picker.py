from datetime import date
from selenium.webdriver.remote.webdriver import WebDriver

from tests.test_date_pickers.helpers import DatePickerBootstrap


def test_date_picker(session: WebDriver):
    """
    Future Dates Disabled
    Days Of Week Disabled- Sunday
    Week Starts from Monday
    Click on 'Today' to select Current date
    Click on Clear button to clear the date entered
    """

    # todo how test will work on Sunday?
    session.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    dp = DatePickerBootstrap(session)
    dp.click()
    dp.today()
    assert dp.get_value() == date.today().strftime("%d/%m/%Y")
