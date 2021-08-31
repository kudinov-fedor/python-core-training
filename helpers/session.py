from selenium import webdriver


def create_session(driver_type="chrome", incognito=True):

    if driver_type == "chrome":
        options = webdriver.ChromeOptions()
        if incognito:
            options.add_argument("--incognito")
        options.add_experimental_option("prefs", {'profile.managed_default_content_settings.media_stream': 1})
        return webdriver.Chrome(executable_path="chromedriver", options=options)

    elif driver_type == "firefox":
        return webdriver.Firefox(executable_path="geckodriver")
