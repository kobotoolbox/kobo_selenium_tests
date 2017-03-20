# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time
from selenium.common.exceptions import NoAlertPresentException

class DeleteAllFormsTest(empty_test.EmptyTest):

    def delete_all_forms(self):
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")
        self.log_prefix = "DeleteAllFormsTest.delete_all_forms"
        self.log_message("Reached, Delete All Forms Test")

        #Hover over the assets action buttons
        form_link = ".asset-row__buttons"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_list = driver.find_elements_by_css_selector(form_link)

        for form in form_link_list:
            self.delete_form()

if __name__ == "__main__":
    unittest.main()
