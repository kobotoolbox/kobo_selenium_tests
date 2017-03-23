# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import unittest
import empty_test

class LogoutTest(empty_test.EmptyTest):

    def test_logout(self):
        try:
            driver = self.driver
            driver.get(self.base_url + "")
            accountBoxSelector = ".account-box"

            #Check if user is logged in
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, accountBoxSelector))

            driver.find_element_by_css_selector(accountBoxSelector).click()

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, '.popover-menu'))

            driver.find_element_by_partial_link_text("Logout").click()

            self.assertTrue( self.is_element_present_with_wait(By.CSS_SELECTOR, accountBoxSelector))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
