# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import unittest
import empty_test


class ImportXlsFormTest(empty_test.EmptyTest):

    def test_import_xls_form(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            self.startNewProject("My Awesome KoboToolbox Form")

            # Complete "Create New Project (step 2 of 2)"
            upload_xls_button_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[text() = 'Upload an XLSForm']")
            ))
            upload_xls_button_el.click()

            # click on the upload button
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".dropzone input[type='file']"))
            xls_file = os.getcwd()+"/My_Awesome_Kobo_Form.xls"
            driver.find_element_by_css_selector(".dropzone input[type='file']").send_keys(xls_file)

            # Make sure the form was uploaded
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='XLS Import completed']"))

            # This is an empty_test method!
            self.generic_preview_form()

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
