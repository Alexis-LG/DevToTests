# content of test_firsttestcase.py

from pytruth.truth.truth import AssertThat

from Page.HomePage import HomePage
from Page.PostPage import PostPage
from Page.SearchPage import SearchPage


def test_is_user_in_website(browser):
    AssertThat(browser.current_url).IsEqualTo("https://dev.to/")


def test_can_user_search_for_posts(browser):
    homepage = HomePage(browser)
    homepage.search_for("must have extensions")
    searchpage = SearchPage(browser)
    searchpage.select_first_result()
    postpage = PostPage(browser)
    AssertThat(postpage.is_readable()).IsTrue()
