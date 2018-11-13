from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 30

    def navigate_to(self, url):
        self.browser.get(url)