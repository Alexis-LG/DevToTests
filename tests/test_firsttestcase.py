# content of test_firsttestcase.py

from pytruth.truth.truth import AssertThat
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_is_user_in_website(browser):
    AssertThat(browser.current_url).IsEqualTo("https://dev.to/")


def test_can_user_search_for_posts(browser):
    search_bar = browser.find_element_by_xpath("//input[@placeholder='search']")
    search_bar.send_keys("must have extensions")
    search_bar.send_keys(Keys.ENTER)
    WebDriverWait(browser, 60).until(expected_conditions.url_contains("https://dev.to/search?q="))
    WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((
        By.XPATH, "//div[contains(@class, 'single-article')][1]//h3")))
    post = browser.find_element_by_xpath("//div[contains(@class, 'single-article')][1]//h3")
    post.click()
    WebDriverWait(browser, 60).until(
        expected_conditions.url_to_be("https://dev.to/chrisvasqm/must-have-extensions-for-vs-code-according-to-me-dho"))
    AssertThat(browser.current_url).IsEqualTo(
        "https://dev.to/chrisvasqm/must-have-extensions-for-vs-code-according-to-me-dho")
