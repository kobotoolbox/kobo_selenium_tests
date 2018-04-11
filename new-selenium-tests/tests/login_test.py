# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import unittest
import empty_test
import traceback

from logout_test import LogoutTest


class LoginTest(empty_test.EmptyTest):

    @staticmethod
    def do_login(test_instance):
        driver = test_instance.driver
        login_url = test_instance.base_url + "accounts/login/?next=/"
        driver.get(login_url)
        print "HIT: " + login_url

        # Make sure the you are on the login page
        test_instance.assertTrue(test_instance.is_element_present_with_wait(By.ID, "id_username"))
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(test_instance.username)

        test_instance.assertTrue(test_instance.is_element_present(By.ID, "id_password"))
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(test_instance.password)

        test_instance.assertTrue(test_instance.is_element_present(By.CSS_SELECTOR, ".registration__action"))
        driver.find_element_by_css_selector(".registration__action").click()
        test_instance.assertTrue(test_instance.is_element_present_with_wait(By.CSS_SELECTOR, ".account-box"))

    def test_login(self):
        try:
            LoginTest.do_login(test_instance=self)
            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)

    def test_login_after_logout(self):
        # TODO: figure out the purpose of this try / except boilerplate
        try:
            LogoutTest.do_logout(test_instance=self)
            LoginTest.do_login(test_instance=self)
            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
