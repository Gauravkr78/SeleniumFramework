from selenium.webdriver.common.by import By
from .base_page import BasePage

class Guru99Page(BasePage):

    # Locators for Guru99 Bank login page
    USER_ID_INPUT = (By.NAME, "uid")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "btnLogin")

    # Locator for Manager ID text on successful login page
    MANAGER_ID_TEXT = (By.XPATH, "//td[contains(text(), 'Manger Id')]")

    # Locators for New Customer Page
    CUSTOMER_NAME = (By.NAME, "name")
    GENDER_MALE = (By.CSS_SELECTOR, "input[value='m']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "input[value='f']")
    DATE_OF_BIRTH = (By.NAME, "dob")
    ADDRESS = (By.NAME, "addr")
    CITY = (By.NAME, "city")
    STATE = (By.NAME, "state")
    PIN = (By.NAME, "pinno")
    MOBILE = (By.NAME, "telephoneno")
    EMAIL = (By.NAME, "emailid")
    PASSWORD_NEW_CUSTOMER = (By.NAME, "password")
    SUBMIT_CUSTOMER = (By.NAME, "sub")

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://demo.guru99.com"

    def load_login_page(self):
        self.driver.get(f"{self.base_url}/v4")

    def load_new_customer_page(self):
        self.driver.get(f"{self.base_url}/v4/manager/addcustomerpage.php")

    # Login page actions
    def enter_user_id(self, user_id):
        self.type(self.USER_ID_INPUT, user_id)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        # Check for presence of Manager ID element on page after login
        try:
            self.wait.until(lambda d: d.find_element(*self.MANAGER_ID_TEXT))
            return True
        except:
            return False

    # New customer page actions
    def create_new_customer(self, customer_data):
        self.type(self.CUSTOMER_NAME, customer_data['name'])

        if customer_data['gender'].lower() == 'male':
            self.click(self.GENDER_MALE)
        else:
            self.click(self.GENDER_FEMALE)

        self.type(self.DATE_OF_BIRTH, customer_data['dob'])
        self.type(self.ADDRESS, customer_data['address'])
        self.type(self.CITY, customer_data['city'])
        self.type(self.STATE, customer_data['state'])
        self.type(self.PIN, customer_data['pin'])
        self.type(self.MOBILE, customer_data['mobile'])
        self.type(self.EMAIL, customer_data['email'])
        self.type(self.PASSWORD_NEW_CUSTOMER, customer_data['password'])

        self.click(self.SUBMIT_CUSTOMER)
