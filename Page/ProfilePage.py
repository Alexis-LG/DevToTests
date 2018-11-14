from Page.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_visible(self):
        profile_name = self.browser.find_element_by_xpath("//span[@itemprop='name']")
        return profile_name.is_displayed()
