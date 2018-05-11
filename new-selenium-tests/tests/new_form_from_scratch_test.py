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

            self.clickSideBarNewBtn()

            self.assertTrue(self.is_element_present_with_wait(By.ID, "name"))
            driver.find_element_by_css_selector("#name").send_keys("My Awesome KoboToolbox Form")

            # fill form description
            description_selector = ".form-modal__item:nth-child(2) textarea"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, description_selector))
            driver.find_element_by_css_selector(description_selector).send_keys("My form's description")

            # select form sector
            sector_input = ".form-modal__item--sector .Select-input input"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, sector_input))
            sector_el = driver.find_element_by_css_selector(sector_input)
            sector_el.send_keys("Public Administration")
            sector_el.send_keys(Keys.ENTER)

            # fill country input
            country_input = ".form-modal__item--country .Select-input input"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, country_input))
            country_el = driver.find_element_by_css_selector(country_input)
            country_el.send_keys("United States")
            country_el.send_keys(Keys.ENTER)

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".form-modal__item--actions button"))
            submit_button = driver.find_element(By.CSS_SELECTOR, ".form-modal__item--actions button")
            submit_button.send_keys(Keys.ENTER)

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
