def scroll_down(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


def forced_click_element(driver, element):
    driver.execute_script('arguments[0].click();', element)
