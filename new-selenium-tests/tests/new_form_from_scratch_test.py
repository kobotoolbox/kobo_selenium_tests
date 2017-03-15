# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import empty_test

class NewFormFromScratchTest(empty_test.EmptyTest):

    def create_new_form_from_scratch(self):
        self.log_prefix = "NewFormFromScratchTest.test_start"
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms/new")
        self.assertTrue(self.is_element_present_with_wait(By.ID, "sidebar-menu", 30))
        el = driver.find_element_by_id("sidebar-menu")
        self.mouse.move_to_element(el).click()

        #fill form name
        new_form_button = driver.find_element_by_css_selector(".collection-nav__link--new")
        self.mouse.move_to_element(new_form_button).click()
        time.sleep(1)
        self.assertTrue(self.is_element_present_with_wait(By.ID, "name"), 30)
        driver.find_element_by_css_selector("#name").send_keys("My Awesome KoboToolbox Form")

        #fill form description
        self.assertTrue(self.is_element_present_with_wait(By.ID, "description"), 30)
        driver.find_element_by_css_selector("#description").send_keys("My form's description")

        #select form sector
        sector_input = ".form-modal__item--sector .Select-input input"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, sector_input), 30)
        sector_el = driver.find_element_by_css_selector(sector_input)
        sector_el.send_keys("Public Administration")
        sector_el.send_keys(Keys.ENTER)
        self.log_message("Sector filled")

        country_input = ".form-modal__item--country .Select-input input"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, country_input), 30)
        country_el = driver.find_element_by_css_selector(country_input)
        country_el.send_keys("United States")
        country_el.send_keys(Keys.ENTER)

        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".form-modal__item--actions button"), 30)
        submit_button = driver.find_element(By.CSS_SELECTOR, ".form-modal__item--actions button")
        submit_button.send_keys(Keys.ENTER)

        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".formBuilder"), 60)

        # WARNING: The 'runScript' command doesn't export to Python, so a manual edit is necessary.
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | window.trackJs && window.trackJs.configure({ userId: "selenium" }) | ]]


if __name__ == "__main__":
    unittest.main()
