# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time


class CustomReports(empty_test.EmptyTest):

    def custom_reports(self):

        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            # Hover over the assets action buttons
            form_link = ".asset-row__celllink--titled"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = driver.find_elements_by_css_selector(form_link)
            form_link_el[0].click()
            print driver.current_url

            # switch to Data tab
            data_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Data']")
            ))
            data_tab_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//span[contains(@class, 'respondents') and contains(text(), 'respondents answered this question.')]"))
            time.sleep(2)

            custom_reports_el = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".popover-menu__toggle")
            ))
            custom_reports_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH,"//a[@class='popover-menu__link' and text()='Create New Report']"))

            new_report_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[@class='popover-menu__link' and text()='Create New Report']")
            ))
            new_report_el.click()

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
