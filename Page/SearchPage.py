from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as Wait

from Page.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def select_first_result(self):
        post = Wait(self.browser, self.timeout).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'single-article')][1]//h3")))
        post.click()
        Wait(self.browser, self.timeout).until(expected_conditions.url_changes(self.browser.current_url))
        pass
