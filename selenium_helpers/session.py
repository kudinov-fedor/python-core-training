import os
from copy import deepcopy

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH", "chromedriver")


def create_session(driver_type="chrome") -> WebDriver:

    if driver_type == "chrome":
        options = webdriver.ChromeOptions()

        # https://chromedriver.chromium.org/capabilities
        options.add_argument("--incognito")
        # options.add_argument("--disable-infobars")
        # options.add_argument("start-maximized")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--disable-popup-blocking")
        # options.add_argument("no-sandbox")
        # options.add_argument("--disable-gpu")
        # options.add_argument("disable-gpu")
        # options.add_argument("--window-size=800,600")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--headless")
        # options.add_argument("no-default-browser-check")
        # options.add_argument("no-first-run")

        prefs = {
            # 'profile.managed_default_content_settings.media_stream': 1,  # allow camera
            # 'profile.default_content_setting_values': {'automatic_downloads': 0},
            # 'profile.content_settings.exceptions': {'automatic_downloads': 0},
            # 'browser.download.manager.showWhenStarting': 0,
            "download.default_directory": os.path.join(os.getcwd(), "tmp")  # specify download directory
        }
        options.add_experimental_option("prefs", prefs)

        # for selenium grid
        capabilities = deepcopy(DesiredCapabilities().CHROME)
        capabilities.update(options.to_capabilities())

        return webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options, desired_capabilities=capabilities)

    elif driver_type == "firefox":
        return webdriver.Firefox(executable_path="geckodriver")
