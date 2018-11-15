from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as Wait

from Page.BasePage import BasePage


class HashtagFeedPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_title_visible(self):
        tag_title = Wait(self.browser, self.timeout).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(@class,'tag-header')]/div/h1")))
        return tag_title.is_displayed()

    def get_feed_filtered_by_hashtag(self, tag):
        feed = self.browser.find_elements_by_xpath("//span[@class='tag' and text()='#" + tag + "']")
        return feed
