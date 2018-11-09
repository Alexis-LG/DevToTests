# content of test_firsttestcase.py
import pytest
from chromedriver_binary.utils import get_chromedriver_path
from pytruth.truth import truth
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver


@pytest.fixture
def setup():
    driver = ChromeDriver(get_chromedriver_path())
    driver.get("https://dev.to/")


@pytest.fixture
def test_is_user_in_website(driver):
    truth.AssertThat(driver.current_url).IsEqualTo("https://dev.to/")


@pytest.fixture
def teardown(self):
    self.driver.close()
