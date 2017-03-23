# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import unittest
import empty_test
import traceback

class LoginTest(empty_test.EmptyTest):

    def test_login(self):
        try:
            driver = self.driver
            driver.get(self.base_url + "accounts/login/?next=/")

            #Make sure the you are on the login page
            self.assertTrue(self.is_element_present_with_wait(By.ID, "id_username"))
            driver.find_element_by_id("id_username").clear()
            driver.find_element_by_id("id_username").send_keys(self.username)

            self.assertTrue(self.is_element_present(By.ID, "id_password"))
            driver.find_element_by_id("id_password").clear()
            driver.find_element_by_id("id_password").send_keys(self.password)

            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, ".registration__action"))
            driver.find_element_by_css_selector(".registration__action").click()
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".account-box"))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
