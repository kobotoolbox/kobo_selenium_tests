# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import unittest
import empty_test

class LogoutTest(empty_test.EmptyTest):

    def test_logout(self):

        self.log_prefix = "LogoutTest.test_logout"
        driver = self.driver
        driver.get(self.base_url + "")
        accountBoxSelector = ".account-box"

        #Check if user is logged in
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, accountBoxSelector, 1))

        self.log_message("Click on "+accountBoxSelector)
        driver.find_element_by_css_selector(accountBoxSelector).click()

        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, '.popover-menu'))

        driver.find_element_by_partial_link_text("Logout").click()

        self.assertTrue( self.is_element_present_with_wait(By.CSS_SELECTOR, accountBoxSelector))

if __name__ == "__main__":
    unittest.main()
