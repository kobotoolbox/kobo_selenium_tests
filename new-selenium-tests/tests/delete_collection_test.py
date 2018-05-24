# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import unittest
import empty_test


class DeleteCollectionTest(empty_test.EmptyTest):

    def delete_collection(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")
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

            delete_collection_selector = "(//a[@data-collection-name='My Wonderful KoboToolbox Collection'])[1]/following-sibling::div/div/a[text()='Delete']"
            delete_collection_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, delete_collection_selector)
            ))
            delete_collection_el.click()

            delete_button_selector = ".ajs-button.ajs-ok"
            # delete_button = self.driver.find_elements_by_css_selector(ok_selector)
            delete_button_el = driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, delete_button_selector)
            ))

            delete_button_el.click()
            time.sleep(3)

            self.assertFalse(
                self.is_element_present_with_wait(
                    By.XPATH,
                    "//a[@data-collection-name='My Wonderful KoboToolbox Collection']",                                                    how_long=3)
            )

            self.status("PASSED")


        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
