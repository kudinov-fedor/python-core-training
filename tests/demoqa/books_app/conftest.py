import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pytest_html import extras

from selenium_helpers.session import create_session


@pytest.fixture(scope="session", params=["chrome"])
def capabilities(request):
    return request.param


@pytest.fixture(scope="session")
def session(capabilities) -> WebDriver:
    session = create_session(capabilities)
    session.implicitly_wait(0.5)
    yield session
    session.quit()


# HTML Report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])
    if report.when == "call" and report.outcome == "failed":
        # extend html report by link to screenshot in case of failure
        driver = item.funcargs["session"]
        driver.save_screenshot("{}.png".format(report.head_line))
        img = extras.image("{}.png".format(report.head_line))
        extra.append(img)

        report.extra = extra


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
