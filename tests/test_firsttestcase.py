# content of test_firsttestcase.py

from pytruth.truth.truth import AssertThat


def test_is_user_in_website(homepage):
    AssertThat(homepage.is_visible()).IsTrue()


def test_can_user_search_for_posts(homepage, searchpage, postpage):
    homepage.search_for("must have extensions")
    searchpage.select_first_result()
    AssertThat(postpage.is_readable()).IsTrue()


def test_can_user_visit_social_links(browser, homepage):
    expected_links = ["https://twitter.com/thepracticaldev",
                      "https://github.com/thepracticaldev",
                      "https://instagram.com/thepracticaldev",
                      "https://facebook.com/thepracticaldev",
                      "https://twitch.tv/thepracticaldev"]

    for link in homepage.get_key_links():
        link.click()
        browser.switch_to.window(browser.window_handles[1])
        AssertThat(expected_links.__contains__(browser.current_url))
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
