from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Page.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def search_for(self, query):
        self.browser.find_element(By.XPATH, "//input[@placeholder='search']").send_keys(query, Keys.ENTER)
        Wait(self.browser, self.timeout).until(expected_conditions.url_contains("https://dev.to/search?q="))
