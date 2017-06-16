# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time
from selenium.common.exceptions import NoAlertPresentException

class DeleteAllFormsTest(empty_test.EmptyTest):

    def delete_all_forms(self):
        try:
            driver = self.driver
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            #Hover over the assets action buttons
            form_link = ".asset-row__buttons"
            # Quick Check
            time.sleep(2)
            if(self.is_element_present(By.CSS_SELECTOR, form_link)):
                form_link_list = driver.find_elements_by_css_selector(form_link)
                for form in form_link_list:
                    self.delete_form()
                    # time.sleep(0.5)

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
