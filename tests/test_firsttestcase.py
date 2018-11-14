# content of test_firsttestcase.py

from pytruth.truth.truth import AssertThat


def test_is_user_in_website(homepage):
    AssertThat(homepage.is_visible()).IsTrue()


def test_can_user_search_for_posts(homepage, searchpage, postpage):
    homepage.search_for("must have extensions")
    searchpage.select_first_result()
    AssertThat(postpage.is_readable()).IsTrue()
