import os, copy

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
USER = os.environ["BOOK_APP_USER"]
PASSWORD = os.environ["BOOK_APP_PASSWORD"]

CAPABILITIES = [
    copy.deepcopy(DesiredCapabilities.CHROME),
    copy.deepcopy(DesiredCapabilities.FIREFOX),
    copy.deepcopy(DesiredCapabilities.OPERA),
]
