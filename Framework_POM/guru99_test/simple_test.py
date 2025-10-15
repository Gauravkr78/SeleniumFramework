from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def quick_guru99_test():
    """Quick test without Page Object Model"""
    driver = webdriver.Chrome()

    try:
        print("🔧 Testing Guru99 Bank demo site...")

        # Login test
        driver.get("https://www.demo.guru99.com/V4/")
        user_id_field = driver.find_element(By.NAME, "uid")
        user_id_field.send_keys("mngr34926")  # Sample UserID, change if needed

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("amUpenu")  # Sample password, change if needed

        login_btn = driver.find_element(By.NAME, "btnLogin")
        login_btn.click()

        # Wait for manager ID to confirm login success
        manager_id_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Manger Id')]"))
        ).text

        print(f"✅ Login successful, found: {manager_id_text}")

        # Navigate to new customer page
        driver.get("https://www.demo.guru99.com/V4/manager/addcustomerpage.php")
        page_title = driver.title
        print(f"✅ New customer page title: {page_title}")

        print("🎉 All tests completed!")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    quick_guru99_test()
