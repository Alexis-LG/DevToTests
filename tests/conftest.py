# conftest.py
import pytest
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    with webdriver.Chrome() as browser:
        print("Creating a Chrome Browser Instance")
        browser.maximize_window()
        browser.get("https://dev.to/")
        print("Opening " + browser.current_url)
        yield browser
