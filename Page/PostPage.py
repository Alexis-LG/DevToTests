from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class PostPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_readable(self):
        title = self.browser.find_element(By.XPATH, "//h1")
        return title.is_displayed()
