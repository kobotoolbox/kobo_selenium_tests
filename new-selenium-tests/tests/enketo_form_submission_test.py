# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time


class EnketoFormSubmissionTest(empty_test.EmptyTest):

    def submit_from_enketo(self):
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

            # switch to form tab
            form_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Form']")
            ))
            form_tab_el.click()

            # click on the More Actions button
            collection_option = ".popover-menu--collectData-menu > a"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, collection_option))
            more_actions_el = driver.find_elements_by_css_selector(collection_option)
            more_actions_el[0].click()

            time.sleep(1)
            #
            # #select enketo link
            enketo_popup_link = "a.popover-menu__link--collect-row[data-method='url']"

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, enketo_popup_link))
            enketo_online_link = self.driver.find_element_by_css_selector(enketo_popup_link)
            enketo_online_link.click()

            time.sleep(1)

            # Open Enketo Link
            open_btn_selector = ".collect-link"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, open_btn_selector))
            # self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".open"))
            enketo_form_link = driver.find_element_by_css_selector(open_btn_selector).get_attribute("href")

            driver.get(enketo_form_link)

            time.sleep(1)
            
            # Make sure form title exists
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "#form-title"))

            # Submit in enketo
            self.fill_out_enketo_form("#submit-form")
            time.sleep(2)

            # Close submission dialog
            submit_btn_selector = "//button[contains(@class, 'vex-dialog-button') and text()='Close']"
            submit_btn_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, submit_btn_selector)
            ))
            submit_btn_el.click()
            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
