# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test

class VerifyNoFormsTest(empty_test.EmptyTest):

    def test_verify_no_forms(self):
        self.driver.implicitly_wait(0)
        self.log_prefix = "VerifyNoFormsTest.preview_form"
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")

        #click on the form link
        form_link = ".asset-row__celllink"
        self.assertFalse(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link, 20))


if __name__ == "__main__":
    unittest.main()
