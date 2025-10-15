from selenium.webdriver.common.by import By
import time


class SauceDemoKeywords:

    def __init__(self, driver):
        self.driver = driver

    # KEYWORDS

    def navigate_to_url(self, url):
        self.driver.get(url)
        return True

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        return True

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        return True

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        return True

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return True

    def verify_login_successful(self):
        time.sleep(2)
        try:
            title = self.driver.find_element(By.CLASS_NAME, "title")
            return "Products" in title.text
        except:
            return False

    def verify_error_message(self, expected_text):
        try:
            error = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
            return expected_text in error.text
        except:
            return False
