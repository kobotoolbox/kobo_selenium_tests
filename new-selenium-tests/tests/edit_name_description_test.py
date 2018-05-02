# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import unittest
import empty_test


class EditNameDescriptionTest(empty_test.EmptyTest):



    def edit_name_description(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            # click into form summary page

            form_link_selector = "//a[@data-kind='asset']/descendant::span[text()[contains(.,'My Awesome KoboToolbox Form')]]"
            form_link_el = self.driver.wait.until(EC.visibility_of_element_located(
                (By.XPATH, form_link_selector)
            ))
            form_link_el.click()

            # select title

            title_input_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='Project title']")
            ))

            # EditTitleDescriptionTest.edit_text(self, title_input_el)

            title_input_el.click()
            time.sleep(2)
            title_input_el.clear()
            time.sleep(2)
            title_input_el.send_keys("My Terrific KoboToolbox Form")
            title_input_el.send_keys(Keys.TAB)
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='successfully updated']"))

            new_name_selector = "//input[@type='text' and @value='My Terrific KoboToolbox Form']"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, new_name_selector))

            # switch to Settings tab
            data_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Settings']")
            ))
            data_tab_el.click()

            # Change title on Settings page
            settings_title_input_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='Enter title of project here']")
            ))
            settings_title_input_el.click()
            time.sleep(1)
            settings_title_input_el.clear()
            time.sleep(1)
            settings_title_input_el.send_keys("My Helpful KoboToolbox Form")
            settings_title_input_el.send_keys(Keys.TAB)

            # Change description on settings page
            description_el = driver.switch_to.active_element
            description_el.clear()
            time.sleep(1)
            description_el.send_keys("My Helpful KoboToolbox Form Description")
            description_el.send_keys(Keys.TAB)
            description_el.submit()


            # Change name back, for consistency with other tests.
            title_input_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@type='text' and @placeholder='Project title']")
            ))
            title_input_el.click()
            time.sleep(2)
            title_input_el.clear()
            time.sleep(2)
            title_input_el.send_keys("My Awesome KoboToolbox Form")
            title_input_el.send_keys(Keys.TAB)
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='successfully updated']"))

            self.status("PASSED")


        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
