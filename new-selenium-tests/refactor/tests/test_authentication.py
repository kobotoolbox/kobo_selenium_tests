# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..settings import USERNAME, PASSWORD, BASE_URL, DRIVER, DRIVER_WAIT_SECS

class AuthenticatedUserTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = DRIVER()
        self.driver.wait = WebDriverWait(self.driver, DRIVER_WAIT_SECS)
        self.driver.maximize_window()
        # Log in
        self.driver.get(BASE_URL)
        username_el = self.driver.find_element(By.NAME, 'username')
        username_el.send_keys(USERNAME)
        password_el = self.driver.find_element(By.NAME, 'password')
        password_el.send_keys(PASSWORD)
        username_el.submit()

    def verify_logged_in(self):
        # `.account-box` only appears after login, so this will raise
        # `TimeoutException` if the login fails
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.account-box')
        ))

class AuthenticationTests(AuthenticatedUserTestCase):
    def test_login(self):
        # Actual login is done by `setUp()`
        self.verify_logged_in()

    def test_logout(self):
        self.verify_logged_in()

        # Log out
        self.driver.find_element_by_css_selector('.account-box').click()
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.popover-menu')
        ))
        self.driver.find_element_by_partial_link_text('Logout').click()

        # Make sure the login screen appears
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.ID, 'id_username')
        ))

