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


class CreateNewCollectionTest(empty_test.EmptyTest):

    def create_new_collection(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")


            # Start new collection
            new_library_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'popover-menu__toggle') and text()='new']")
            ))
            new_library_el.click()

            # Select Collection
            new_collection_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'popover-menu__link') and text()='collection']")
            ))
            new_collection_el.click()


            # Enter name
            input_selector = "input.ajs-input"
            input_el = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, input_selector)
            )).send_keys("My Wonderful KoboToolbox Collection")



            # click the Create Collection button
            create_collection_selector = "//button[text()='Create collection']"
            create_collection_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, create_collection_selector)
            ))
            create_collection_el.click()
            time.sleep(2)
            new_collection_present_selector = "//a[@data-collection-name='My Wonderful KoboToolbox Collection']"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, new_collection_present_selector))

            self.status("PASSED")



        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
