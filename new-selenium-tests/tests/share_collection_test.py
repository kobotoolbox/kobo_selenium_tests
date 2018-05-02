# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import os
import unittest
import empty_test
from logout_test import LogoutTest
from login_test import LoginTest


class ShareCollectionTest(empty_test.EmptyTest):

    @staticmethod
    def wait_for_correct_current_url(self, desired_url):
        self.driver.wait.until(
            lambda driver: driver.current_url == desired_url)

    def share_collection(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")
            ShareCollectionTest.wait_for_correct_current_url(self, self.base_url + "#/library")

            collection_selector = "(//a[@data-collection-name='My Wonderful KoboToolbox Collection'])[1]"
            collection_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, collection_selector)
            ))
            collection_el.click()

            popover_menu__toggle_selector = "(//a[@data-collection-name='My Wonderful KoboToolbox Collection'])[1]/following-sibling::div/a"
            popover_menu__toggle_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, popover_menu__toggle_selector)
            ))
            popover_menu__toggle_el.click()

            share_collection_selector = "(//a[@data-collection-name='My Wonderful KoboToolbox Collection'])[1]/following-sibling::div/div/a[text()='Share']"
            share_collection_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, share_collection_selector)
            ))
            share_collection_el.click()

            user_selector = "//input[@id='permsUser']"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, user_selector))
            user_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, user_selector)
            ))
            user_el.clear()
            user_el.send_keys(self.username2)

            share_button_selector = ".mdl-button--raised.mdl-button--colored"
            # delete_button = self.driver.find_elements_by_css_selector(ok_selector)
            share_button_el = driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, share_button_selector)
            ))
            time.sleep(4)
            share_button_el.click()
            time.sleep(2)


            self.assertTrue(self.is_element_present_with_wait(By.XPATH,
                            "//div[@class='user-row__name'][contains(text(),'selenium_test_2')]",
                            how_long=4)
                            )

            try:
                LogoutTest.do_logout(test_instance=self)
                LoginTest.do_login(test_instance=self, account_name='selenium_test_2')

            except Exception as e:
                self.handle_test_exceptions(e)

            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")
            ShareCollectionTest.wait_for_correct_current_url(self, self.base_url + "#/library")

            time.sleep(2)
            self.assertTrue(self.is_element_present_with_wait(By.XPATH,
                                "//a[@data-collection-name='My Wonderful KoboToolbox Collection']",
                                how_long=3))

            try:
                LogoutTest.do_logout(test_instance=self)
                LoginTest.do_login(test_instance=self, account_name='selenium_test')

            except Exception as e:
                self.handle_test_exceptions(e)
            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
