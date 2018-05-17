# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time


class CustomReports(empty_test.EmptyTest):

    def custom_reports(self):

        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)

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
            # time.sleep(2)

            custom_reports_el = driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".popover-menu--custom-reports")
            ))
            custom_reports_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH,"//a[@class='popover-menu__link' and text()='Create New Report']"))

            new_report_el = driver.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//a[@class='popover-menu__link' and text()='Create New Report']")
            ))
            new_report_el.click()
            text_input_el = driver.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@name='title' and @placeholder='Untitled Report']")
            ))
            text_input_el.send_keys("My Custom Report")

            time.sleep(2)
            text_input_el.send_keys(Keys.TAB)  # tab over to not-visible element

            first_checkbox_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='chart_question'])[1]")
            ))
            first_checkbox_el.send_keys(Keys.SPACE)

            text_input_el.send_keys(Keys.TAB + Keys.TAB + Keys.TAB)
            last_checkbox_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//input[@name='chart_question'])[last()]")
            ))
            last_checkbox_el.send_keys(Keys.SPACE)

            save_button_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//button[contains(@class, 'mdl-button--raised') and text()='Save']")
            ))
            save_button_el.click()

            # Four assertions to signal that
            # the page contains "My Custom Report," "Gender" and "Name" and does not contain "LastName"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH,"//a[@class='popover-menu__toggle' and text()='My Custom Report']"))

            self.assertTrue(
                self.is_element_present_with_wait(
                    By.XPATH,
                    "//h2[text()='Name']",
                    how_long=3
                )
            )
            self.assertTrue(
                self.is_element_present_with_wait(
                    By.XPATH,
                    "//h2[text()='Gender']",
                    how_long=3
                )
            )
            self.assertFalse(
                self.is_element_present_with_wait(
                    By.XPATH,
                    "//h2[text()='LastName']",
                    how_long=3
                )
            )
            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
