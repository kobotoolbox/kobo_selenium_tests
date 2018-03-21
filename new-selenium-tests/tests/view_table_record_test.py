# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time


class ViewTableRecordTest(empty_test.EmptyTest):

    def view_table_record(self):

        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            # Hover over the assets action buttons
            form_link = ".asset-row__celllink--titled"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = driver.find_elements_by_css_selector(form_link)
            form_link_el[0].click()
            print driver.current_url

            # switch to Data tab
            data_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Data']")
            ))
            data_tab_el.click()

            # select Table
            download_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab undefined') and text()='Table']")
            ))
            download_el.click()

            # click open link
            open_el = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.rt-link')
            ))
            open_el.click()

            # ensure that there is a table with a question and a response
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "table"))
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".submission--question"))
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".submission--response"))


            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
