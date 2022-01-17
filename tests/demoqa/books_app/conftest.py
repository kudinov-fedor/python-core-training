import sys
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pytest_html import extras

from tests.demoqa.books_app.api_client import ApiClient
from tests.demoqa.books_app.constants import USER, PASSWORD

from selenium_helpers.session import create_session
from .pageobject import BasePage, LoginPage, BooksPage, ProfilePage, BookPage  # noqa: F401


@pytest.fixture(scope="session", params=["chrome"])
def capabilities(request):
    return request.param


@pytest.fixture(scope="session", autouse=True)
def session(capabilities) -> WebDriver:
    session = create_session(capabilities)
    session.implicitly_wait(0.5)
    yield session
    session.quit()


@pytest.fixture(autouse=True)
def clear_cache(session):
    session.delete_all_cookies()
    session.refresh()


@pytest.fixture(autouse=True)
def user():
    user = ApiClient(USER, PASSWORD)
    user.create()
    yield user
    user.reset()


# HTML Report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])
    if report.when == "call" and report.outcome == "failed":
        # extend html report by link to screenshot in case of failure
        if "session" not in item.funcargs:
            return

        driver = item.funcargs["session"]
        driver.save_screenshot("{}.png".format(report.head_line))
        img = extras.image("{}.png".format(report.head_line))
        extra.append(img)
        report.extra = extra

        # attach screenshot to allure report
        try:
            import allure
            allure.attach.file("./{}.png".format(report.head_line), attachment_type=allure.attachment_type.PNG)
        except ImportError:
            pass

        # fail step for test project
        try:
            from src.testproject.decorator.report_assertion_errors import __handle_step_report_details
            description, message = __handle_step_report_details(description=repr(sys.last_value),
                                                                message="Assertion failed")
            driver.report().step(description=description,
                                 message=message,
                                 passed=False,
                                 screenshot=True)
        except ImportError:
            pass


# HTML HOOKS
from py.xml import html


def pytest_html_report_title(report):
    report.title = "My very own title!"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.h1("MY GREAT PREFIX")])


def pytest_html_results_table_header(cells):
    # Called after building results table header.
    ...


def pytest_html_results_table_html(report, data):
    # Called after building results table additional HTML.
    ...


def pytest_html_results_table_row(report, cells):
    # Called after building results table row.
    ...
