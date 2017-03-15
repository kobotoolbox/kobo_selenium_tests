# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import unittest
import empty_test

class LoginTest(empty_test.EmptyTest):

    def test_login(self):
        self.log_prefix ="LoginTest.test_login"
        driver = self.driver
        driver.get(self.base_url + "accounts/login/?next=/")

        #Make sure the you are on the login page
        self.assertTrue(self.is_element_present_with_wait(By.ID, "id_username", 10))
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(self.username)
        self.log_message("username filled")
        self.assertTrue(self.is_element_present(By.ID, "id_password"))
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(self.password)
        self.log_message("password filled")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".registration__action"))
        self.log_message("Found .registration__action")
        driver.find_element_by_css_selector(".registration__action").click()
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".account-box", 30))
        # WARNING: The 'runScript' command doesn't export to Python, so a manual edit is necessary.
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | window.trackJs && window.trackJs.configure({ userId: "selenium" }) | ]]


if __name__ == "__main__":
    unittest.main()
