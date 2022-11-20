class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def send_text(self, text, *locator):
        self.get_element(*locator).send_keys(text)

    def left_click(self, *locator):
        self.get_element(*locator).click()