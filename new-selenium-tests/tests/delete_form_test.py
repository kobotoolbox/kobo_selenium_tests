# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time
from selenium.common.exceptions import NoAlertPresentException

class DeleteFormTest(empty_test.EmptyTest):

    def delete_form(self):
        self.log_prefix = "DeleteFormTest.delete_form"
        self.log_message("Reached, Delete Form Test")
        self.driver.get(self.base_url + "#/forms")
        #called from emptyTest
        self.delete_form()

if __name__ == "__main__":
    unittest.main()
