# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test

class VerifyNoFormsTest(empty_test.EmptyTest):

    def test_verify_no_forms(self):
        driver = self.driver
        driver.implicitly_wait(0)
        self.log_prefix = "VerifyNoFormsTest.test_verify_no_forms"
        self.log_message("Reached, Verify that no forms exist Test")
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")
        form_submissions = driver.find_elements_by_css_selector('.asset-row__celllink')
        if len(form_submissions):
            raise Exception("Verify no forms exists has failed because one or more forms still exist")

if __name__ == "__main__":
    unittest.main()
