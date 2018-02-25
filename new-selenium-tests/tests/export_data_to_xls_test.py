# -*- coding: utf-8 -*-
from selenium                                       import webdriver
from selenium.webdriver.support                     import expected_conditions as EC
from selenium.webdriver.common.by                   import By
import unittest
import empty_test
import time

class ExportDataToXls(empty_test.EmptyTest):

    def export_data(self):

        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            #Hover over the assets action buttons
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

            download_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab undefined') and text()='Downloads']")
            ))
            download_el.click()

            # driver.get(driver.current_url.replace("/landing", "/data/downloads"))

            #make sure you're on the data/downloads page
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//label[text()='Select export type']"))

            #make sure the submit button exists
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "input[type='submit']"))

            driver.find_element_by_css_selector("input[type='submit']").click()

            time.sleep(2)

            # Make sure the file was downloaded?
            if isinstance(self.driver, webdriver.Remote):
                # When using a remote `webdriver`, we don't have direct access to downloaded files.
                #   Instead, inspect the remote Selenium server's filesystem with its browser.
                driver.get('file:///tmp/')
            #     # TODO: Fix this kludge with a pure Xpath solution?
                # local_file_link = driver.find_element_by_partial_link_text('My_Awesome_Kobo_Form')
                local_file_link = driver.find_element_by_partial_link_text('.xls')
                file_size =  local_file_link.find_element_by_xpath('../../td[2]').text
                self.status('Downloaded {} file `{}`.'.format(file_size, local_file_link.text))
            elif not self.does_file_exist_with_wildcard("/tmp/My_Awesome_Kobo_Form.xls"):
                raise Exception("File was not downloaded")

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
