# conftest.py
import pytest
from chromedriver_binary.utils import get_chromedriver_filename
from selenium import webdriver

from Page.HomePage import HomePage
from Page.PostPage import PostPage
from Page.ProfilePage import ProfilePage
from Page.SearchPage import SearchPage


@pytest.fixture(autouse=True)
def browser():
    with webdriver.Chrome(get_chromedriver_filename()) as browser:
        print("Creating a Chrome Browser Instance")
        browser.maximize_window()
        browser.get("https://dev.to/")
        print("Opening " + browser.current_url)
        yield browser


@pytest.fixture()
def homepage(browser):
    return HomePage(browser)


@pytest.fixture()
def searchpage(browser):
    return SearchPage(browser)


@pytest.fixture()
def postpage(browser):
    return PostPage(browser)


@pytest.fixture()
def profilepage(browser):
    return ProfilePage(browser)
