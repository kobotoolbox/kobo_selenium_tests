# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os
import unittest
import empty_test


class SubscribeLibraryCollectionTest(empty_test.EmptyTest):

    def subscribe_library_collection(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")

            # Click on Public Collections
            public_collections_selector = "//div[contains(@class, 'form-sidebar__label') and text()='Public Collections']"
            public_collections_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, public_collections_selector)
            ))
            public_collections_el.click()

            # Subscribe to specific collection - Step 1 of 3
            library_block_selector = "//span[@class='form-sidebar__iteminner' and text()='Sample Library Blocks']"
            library_block_selector_el = driver.wait.until(EC.visibility_of_element_located(
                (By.XPATH, library_block_selector)
            ))
            library_block_selector_el.click()

            # Subscribe to specific collection - Step 2 of 3
            subscribe_icon_selector = ".k-icon-more"
            subscribe_icon_el = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, subscribe_icon_selector)
            ))
            subscribe_icon_el.click()

            # Subscribe to specific collection - Step 3 of 3
            subscribe_selector = "//a[text()='subscribe']"
            subscribe_el = driver.find_elements_by_xpath(subscribe_selector)
            if len(subscribe_el) == 1 and subscribe_el[0].is_displayed():
                subscribe_el[0].click()
            elif len(subscribe_el) == 2 and subscribe_el[0].is_displayed():  # Already Subscribed
                pass

            # Assert that collection is displayed
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//a[@data-collection-name='Sample Library Blocks']"))

            self.status("PASSED")

            # TODO: Unsubscribe to prepare for next time

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
