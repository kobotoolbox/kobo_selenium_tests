# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = 'selenium_test'
PASSWORD = USERNAME # well, i'll be!
KPI_BASE_URL = 'https://kf.kobotoolbox.org/'

class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.wait = WebDriverWait(self.driver, 5)

    def test_login(self):
        self.driver.get(KPI_BASE_URL)
        username_el = self.driver.find_element(By.NAME, 'username')
        username_el.send_keys(USERNAME)
        password_el = self.driver.find_element(By.NAME, 'password')
        password_el.send_keys(PASSWORD)
        username_el.submit()
        self.assertTrue(self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".account-box")
        )))

if __name__ == "__main__":
    unittest.main()




'''



from selenium.webdriver.common.by import By
import unittest
import traceback


class LoginTest(empty_test.EmptyTest):

    @staticmethod
    def do_login(test_instance, account_name='selenium_test'):
        driver = test_instance.driver
        login_url = test_instance.base_url + "accounts/login/?next=/"
        driver.get(login_url)
        print "HIT: " + login_url

        # Make sure the you are on the login page
        test_instance.assertTrue(test_instance.is_element_present_with_wait(By.ID, "id_username"))
        driver.find_element_by_id("id_username").clear()
        if account_name == 'selenium_test_2':
            driver.find_element_by_id("id_username").send_keys(account_name)

        else:
            driver.find_element_by_id("id_username").send_keys(test_instance.username)

        test_instance.assertTrue(test_instance.is_element_present(By.ID, "id_password"))
        driver.find_element_by_id("id_password").clear()
        if account_name == 'selenium_test_2':
            driver.find_element_by_id("id_password").send_keys('selenium_test_2')
        else:
            print account_name
            driver.find_element_by_id("id_password").send_keys(account_name)

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
'''