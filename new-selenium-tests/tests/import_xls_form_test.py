# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import unittest
import empty_test

class ImportXlsFormTest(empty_test.EmptyTest):

    def test_import_xls_form(self):
        self.log_prefix = "ImportXlsFormTest.test_import_xls_form"
        self.log_message("Reached")
        driver = self.driver
        driver.implicitly_wait(0)
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")

        self.assertTrue(self.is_element_present_with_wait(By.ID, "sidebar-menu"))
        sidebar = driver.find_element_by_id("sidebar-menu")
        sidebar.click()
        sleep(1)
        

        #click on the upload button
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".dropzone input[type='file']"))
        xls_file = os.getcwd()+"/My Awesome Kobo Form.xls"
        driver.find_element_by_css_selector(".dropzone input[type='file']").send_keys(xls_file)

        #Make sure the form was uploaded
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".form-view__label--title"))
        #This is an empty_test method!
        self.generic_preview_form()

if __name__ == "__main__":
    unittest.main()
