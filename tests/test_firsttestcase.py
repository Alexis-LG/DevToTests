# content of test_firsttestcase.py

from pytruth.truth.truth import AssertThat

from Utils.Screenshot_Utils import take_screenshot


def test_is_user_in_website(homepage):
    AssertThat(homepage.is_visible()).IsTrue()


def test_can_user_search_for_posts(browser, homepage, searchpage, postpage):
    homepage.search_for("must have extensions")
    searchpage.select_first_result()
    AssertThat(postpage.is_readable()).IsTrue()
    take_screenshot(browser)


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


def test_can_check_user_profile(homepage, searchpage, profilepage):
    homepage.search_for("Ben Halpern")
    searchpage.select_first_result()
    AssertThat(profilepage.is_visible()).IsTrue()


def test_can_sort_feed_by_latest(homepage):
    homepage.filter_posts_by_latest()
    AssertThat(homepage.is_latest_feed_visible()).IsTrue()


def test_can_access_hashtags(homepage, hashtagfeedpage):
    homepage.filter_by_hashtag("python")
    AssertThat(hashtagfeedpage.is_title_visible()).IsTrue()
    for tag in hashtagfeedpage.get_feed_filtered_by_hashtag("python"):
        AssertThat(tag.is_displayed()).IsTrue()
