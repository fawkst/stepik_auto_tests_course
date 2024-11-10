import unittest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class TestRegister(unittest.TestCase):
    LINK1 = "http://suninjuly.github.io/registration1.html"
    LINK2 = "http://suninjuly.github.io/registration2.html"

    @staticmethod
    def register_test(link):
        try:
            browser = Chrome()
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, '.first_block>.first_class input')
            first_name.send_keys('test first name')

            last_name = browser.find_element(By.CSS_SELECTOR, '.first_block>.second_class input')
            last_name.send_keys('test last name')

            email = browser.find_element(By.CSS_SELECTOR, '.first_block>.third_class input')
            email.send_keys('test@test')

            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            time.sleep(1)
            return browser.find_element(By.TAG_NAME, "h1").text
        finally:
            browser.quit()

    def test_registration1(self):
        self.assertEqual(self.register_test(self.LINK1), "Congratulations! You have successfully registered!", "Failed register1 test)")

    def test_registration2(self):
        self.assertEqual(self.register_test(self.LINK2), "Congratulations! You have successfully registered!", "Failed register1 test)")


if __name__ == "__main__":
    unittest.main()
