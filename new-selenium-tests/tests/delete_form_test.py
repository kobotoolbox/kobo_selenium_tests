# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time
from selenium.common.exceptions import NoAlertPresentException

class DeleteFormTest(empty_test.EmptyTest):

    def delete_form(self):
        try:
            self.driver.get(self.base_url + "#/forms")
            #called from emptyTest
            self.delete_form()
            self.status("PASSED")
            
        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
