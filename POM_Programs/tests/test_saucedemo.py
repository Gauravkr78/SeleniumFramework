import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestSauceDemo:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        login_page = LoginPage()
        login_page.open(driver)
        login_page.login(driver, "standard_user", "secret_sauce")

        inventory_page = InventoryPage()

        # Assertion 1: URL contains "inventory"
        assert "inventory" in inventory_page.get_current_url(driver)

        # Assertion 2: Page title is "Products"
        assert inventory_page.get_page_title(driver) == "Products"

        # Assertion 3: At least one inventory item is displayed
        assert inventory_page.get_inventory_count(driver) > 0
