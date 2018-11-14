# conftest.py
import pytest
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.wait import WebDriverWait

from Page.HomePage import HomePage
from Page.PostPage import PostPage
from Page.SearchPage import SearchPage


@pytest.fixture(autouse=True)
def browser():
    with webdriver.Chrome() as browser:
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
