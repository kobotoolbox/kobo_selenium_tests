# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException # NoSuchElementException, TimeoutException

from logout_test import LogoutTest
from login_test import LoginTest
from share_project_form_landing_test import ShareProjectFormLandingTest

import unittest
import empty_test
import time


class RemoveSharedUserTest(empty_test.EmptyTest):

    @staticmethod
    def navigate_to_summary_page(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.get(self.base_url + "#/forms")
            time.sleep(2)

            # Click the title
            form_link = ".asset-row__celllink--titled"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = driver.find_elements_by_css_selector(form_link)
            form_link_el[0].click()
            print driver.current_url

        except Exception as e:
            self.handle_test_exceptions(e)

    @staticmethod
    def wait_for_correct_current_url(self, desired_url):
        self.driver.wait.until(
            lambda driver: driver.current_url == desired_url)

    def remove_shared_user(self):
        try:

            RemoveSharedUserTest.navigate_to_summary_page(self)

            time.sleep(2)

            share_link_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'popover-menu__link') and text()='Share form']")
            ))
            share_link_el.click()

            # Remove the shared account
            trash_icon_selector = ".k-icon-trash"
            # self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, trash_icon_selector))
            trash_icon_el = self.driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, trash_icon_selector)
            ))
            trash_icon_el.click()
            time.sleep(2)
            # TODO: check with John if this assertion is appropriate
            body_text = self.driver.find_element_by_tag_name('body').text
            self.assertNotIn("the text you want to check for", body_text)

            # TODO: Deselect the share_by_link_checkbox

            close_record_detail_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[@class='modal-x']")
            ))
            close_record_detail_el.click()

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
