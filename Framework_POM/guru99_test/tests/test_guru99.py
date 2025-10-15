import pytest
from selenium import webdriver
from pages.guru99_page import Guru99Page

class TestGuru99:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.guru_page = Guru99Page(self.driver)
        yield
        self.driver.quit()

    def test_login(self):
        """Test login with valid credentials"""
        self.guru_page.load_login_page()
        self.guru_page.enter_user_id("mngr34926")  # sample user ID, replace if needed
        self.guru_page.enter_password("amUpenu")   # sample password, replace if needed
        self.guru_page.click_login()

        assert self.guru_page.is_login_successful(), "Login failed"

    def test_new_customer_registration(self):
        """Test new customer registration"""
        self.guru_page.load_login_page()
        self.guru_page.enter_user_id("mngr34926")
        self.guru_page.enter_password("amUpenu")
        self.guru_page.click_login()

        assert self.guru_page.is_login_successful(), "Login failed"

        self.guru_page.load_new_customer_page()

        customer_data = {
            'name': 'John Doe',
            'gender': 'male',
            'dob': '1990-01-01',
            'address': '123 Main St',
            'city': 'New York',
            'state': 'NY',
            'pin': '123456',
            'mobile': '1234567890',
            'email': 'john.doe@example.com',
            'password': 'password123'
        }

        self.guru_page.create_new_customer(customer_data)

        # Verify success message on page
        assert "Customer Registered Successfully" in self.driver.page_source
