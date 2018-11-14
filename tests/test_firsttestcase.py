# content of test_firsttestcase.py

from pytruth.truth.truth import AssertThat


def is_user_in_website(browser):
    AssertThat(browser.current_url).IsEqualTo("https://dev.to/")


def test_can_user_search_for_posts(homepage, searchpage, postpage):
    homepage.search_for("must have extensions")
    searchpage.select_first_result()
    AssertThat(postpage.is_readable()).IsTrue()
