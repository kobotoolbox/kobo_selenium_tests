# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import unittest
import empty_test


class LogoutTest(empty_test.EmptyTest):

    @staticmethod
    def do_logout(test_instance):
        driver = test_instance.driver
        driver.get(test_instance.base_url + "")
        accountBoxSelector = ".account-box"

        # Check if user is logged in
        test_instance.assertTrue(test_instance.is_element_present_with_wait(By.CSS_SELECTOR, accountBoxSelector))

        driver.find_element_by_css_selector(accountBoxSelector).click()

        test_instance.assertTrue(test_instance.is_element_present_with_wait(By.CSS_SELECTOR, '.popover-menu'))

        driver.find_element_by_partial_link_text("Logout").click()

        # Make sure the login screen appears
        test_instance.assertTrue(test_instance.is_element_present_with_wait(By.ID, "id_username"))

    def test_logout(self):
        try:
            LogoutTest.do_logout(test_instance=self)
            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
