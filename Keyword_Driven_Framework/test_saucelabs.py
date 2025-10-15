from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from keywords import SauceDemoKeywords
from config import Config
import pytest


class TestSauceDemo:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.kw = SauceDemoKeywords(self.driver)
        yield
        self.driver.quit()

    def test_valid_login(self):
        """Test valid login using keywords"""
        self.kw.navigate_to_url(Config.BASE_URL)
        self.kw.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        assert self.kw.verify_login_successful() is True

    def test_invalid_login(self):
        """Test invalid login using keywords"""
        self.kw.navigate_to_url(Config.BASE_URL)
        self.kw.login("invalid_user", "wrong_password")
        assert self.kw.verify_error_message("do not match") is True
