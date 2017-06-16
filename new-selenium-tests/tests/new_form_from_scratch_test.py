# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import empty_test

class NewFormFromScratchTest(empty_test.EmptyTest):

    def create_new_form_from_scratch(self):
        try :
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            #go to enwe form page and click on the sidbar menu
            driver.get(self.base_url + "#/forms")
            driver.maximize_window()

            self.clickSideBarNewBtn()

            new_project_btn_selector = ".form-sidebar__wrapper .popover-menu__content--visible > .popover-menu__link"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, new_project_btn_selector))
            new_project_btn = driver.find_element_by_css_selector(new_project_btn_selector)
            new_project_btn.click()

            self.assertTrue(self.is_element_present_with_wait(By.ID, "name"))
            driver.find_element_by_css_selector("#name").send_keys("My Awesome KoboToolbox Form")

            #fill form description
            description_selector= ".form-modal__item:nth-child(2) textarea"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, description_selector))
            driver.find_element_by_css_selector(description_selector).send_keys("My form's description")

            #select form sector
            sector_input = ".form-modal__item--sector .Select-input input"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, sector_input))
            sector_el = driver.find_element_by_css_selector(sector_input)
            sector_el.send_keys("Public Administration")
            sector_el.send_keys(Keys.ENTER)

            #fill country input
            country_input = ".form-modal__item--country .Select-input input"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, country_input))
            country_el = driver.find_element_by_css_selector(country_input)
            country_el.send_keys("United States")
            country_el.send_keys(Keys.ENTER)

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".form-modal__item--actions button"))
            submit_button = driver.find_element(By.CSS_SELECTOR, ".form-modal__item--actions button")
            submit_button.send_keys(Keys.ENTER)

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".formBuilder"))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)



if __name__ == "__main__":
    unittest.main()
