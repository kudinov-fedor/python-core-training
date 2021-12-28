import os
import json
from copy import deepcopy

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH", "chromedriver")
ANDROID_CHROME_DRIVER_PATH = os.environ.get("ANDROID_CHROME_DRIVER_PATH", "chromedriver")
FIREFOX_DRIVER_PATH = os.environ.get("FIREFOX_DRIVER_PATH", "geckodriver")
SAFARI_DRIVER_PATH = os.environ.get("SAFARI_DRIVER_PATH", "/usr/bin/safaridriver")
OPERA_DRIVER_PATH = os.environ.get("OPERA_DRIVER_PATH", "operadriver")
CONFIG = os.environ.get("CONFIG")


def create_session(driver_type="chrome", config: dict = None) -> WebDriver:

    # selenium grid
    if CONFIG:
        with open(CONFIG) as f:
            caps = json.loads(f.read())
            caps.update(config or {})
        return webdriver.remote.webdriver.WebDriver(desired_capabilities=caps)

    elif driver_type == "chrome":
        options = webdriver.ChromeOptions()

        # https://chromedriver.chromium.org/capabilities
        # options.add_argument("--start-maximized")  # Opens Chrome in maximize mode
        # options.add_argument("--incognito")  # Opens Chrome in incognito mode
        # options.add_argument("--headless")  # Opens Chrome in headless mode
        # options.add_argument("--disable-extensions")  # Disables existing extensions on Chrome browser
        # options.add_argument("--disable-popup-blocking")  # Disables pop-ups displayed on Chrome browser
        # options.add_argument("--make-default-browser")  # Makes Chrome default browser
        # options.add_argument("--version")  # Prints chrome browser version

        # options.add_argument("--disable-infobars")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--no-default-browser-check")
        # options.add_argument("--no-first-run")

        # todo clean up new tab opened
        options.add_extension(os.path.join(os.getcwd(), "extensions", "add_blocker.crx"))

        prefs = {
            'profile.managed_default_content_settings.media_stream': 1,  # allow camera
            # 'profile.default_content_setting_values': {'automatic_downloads': 0},
            # 'profile.content_settings.exceptions': {'automatic_downloads': 0},
            # 'browser.download.manager.showWhenStarting': 0,
            "download.default_directory": os.path.join(os.getcwd(), "tmp")  # specify download directory
        }
        options.add_experimental_option("prefs", prefs)

        # remove notification ‘Chrome is being controlled by ...
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # for selenium grid
        capabilities = deepcopy(DesiredCapabilities().CHROME)
        capabilities.update(options.to_capabilities())

        return webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options, desired_capabilities=capabilities)

    elif driver_type == "firefox":
        return webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)

    elif driver_type == "safari":
        return webdriver.Safari(SAFARI_DRIVER_PATH)

    elif driver_type == "opera":
        return webdriver.Opera(executable_path=OPERA_DRIVER_PATH,
                               desired_capabilities=deepcopy(DesiredCapabilities.OPERA))

    elif driver_type == "android":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('androidPackage', 'com.android.chrome')
        driver = webdriver.Chrome(ANDROID_CHROME_DRIVER_PATH, chrome_options=options)
        return driver
