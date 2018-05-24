# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
import empty_test


class NewFormFromScratchTest(empty_test.EmptyTest):

    def create_new_form_from_scratch(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            self.mouse = webdriver.ActionChains(self.driver)
            # go to new form page and click on the sidebar menu
            driver.get(self.base_url + "#/forms")
            driver.maximize_window()

            self.startNewProject("My Awesome KoboToolbox Form")

            # Complete "Create New Project (step 2 of 2)"
            design_button_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[text() = 'Design in Form Builder']")
            ))
            design_button_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".formBuilder"))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
