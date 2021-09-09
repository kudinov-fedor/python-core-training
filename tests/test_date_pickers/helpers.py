from selenium.webdriver.remote.webdriver import WebDriver, WebElement, By


class DatePickerBootstrap:
    field = By.CSS_SELECTOR, "#sandbox-container1 input"
    button = By.CSS_SELECTOR, "#sandbox-container1 span"

    pannels = By.CSS_SELECTOR, ".datepicker.datepicker-dropdown > div"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self):
        self.driver.find_element(*self.field).click()

    def send_value(self, value):
        self.driver.find_element(*self.field).send_keys(value)

    def get_value(self):
        return self.driver.find_element(*self.field).get_attribute("value")

    # interaction with active panel

    def get_active_panel(self) -> WebElement:
        for active_element in self.driver.find_elements(*self.pannels):
            if active_element.value_of_css_property("display") == "block":
                return active_element
        raise AssertionError("No active element found")

    def up(self):
        self.get_active_panel().find_element(By.CSS_SELECTOR, ".datepicker-switch").click()

    def left(self):
        self.get_active_panel().find_element(By.CSS_SELECTOR, "th.prev").click()

    def right(self):
        self.get_active_panel().find_element(By.CSS_SELECTOR, "th.prev").click()

    def get_header(self) -> str:
        return self.get_active_panel().find_element(By.CSS_SELECTOR, ".datepicker-switch").text

    def today(self):
        self.get_active_panel().find_element(By.CSS_SELECTOR, ".today").click()

    def clear(self):
        self.get_active_panel().find_element(By.CSS_SELECTOR, ".clear").click()

    def get_rows(self):
        return self.get_active_panel().find_elements(By.CSS_SELECTOR, "table.table-condensed tbody tr")

    def get_cells(self, *, value: str = None, class_name: str = ""):
        from itertools import chain

        rows = self.get_rows()
        cells = chain.from_iterable(r.find_elements(By.CSS_SELECTOR, "td") for r in rows)
        if value:
            return [c for c in cells if c.text == value and c.get_attribute("class") == class_name]
        return list(cells)

    def get_cells_by_class(self, *, value: str = None):
        from collections import defaultdict
        cells = self.get_cells(value=value)
        res = defaultdict(list)
        for cell in cells:
            res[cell.get_attribute("class")].append(cell)
        return res


class FromDatePickerBootstrap(DatePickerBootstrap):
    field = By.CSS_SELECTOR, "#datepicker > input.form-control:nth-child(1)"


class ToDatePickerBootstrap(DatePickerBootstrap):
    field = By.CSS_SELECTOR, "#datepicker > input.form-control:nth-child(3)"
