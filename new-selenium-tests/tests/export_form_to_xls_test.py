# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time

class ExportFormToXlsTest(empty_test.EmptyTest):

    def export_form_to_xls(self):
        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            #Hover over the assets action buttons
            form_link = ".asset-row__buttons"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = driver.find_elements_by_css_selector(form_link)
            self.mouse.move_to_element(form_link_el[0]).move_by_offset(0,1).perform()
            time.sleep(2)

            #click on the More Actions button
            more_actions_button = "button[data-tip='More Actions']"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, more_actions_button))
            more_actions_el = driver.find_elements_by_css_selector(more_actions_button)
            more_actions_el[0].click()
            time.sleep(2)

            #click on the Download as XLS button
            xls_link_selector = ".popover-menu__link.popover-menu__link--dl-xls"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, xls_link_selector))
            xls_link = self.driver.find_elements_by_css_selector(xls_link_selector)
            xls_link[0].click()

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
