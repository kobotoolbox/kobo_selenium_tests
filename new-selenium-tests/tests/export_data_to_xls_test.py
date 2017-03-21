# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time

class ExportDataToXls(empty_test.EmptyTest):

    def export_data(self):
        self.log_prefix = "ExportDataToXls.deploy_form"
        self.log_message("Reached, Export Data to XLS Test")
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")

        #Hover over the assets action buttons
        form_link = ".asset-row__celllink--titled"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_el = driver.find_elements_by_css_selector(form_link)
        form_link_el[0].click()

        #click on the DATA dropdown
        data_dropdown = "#more-data-tab"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, data_dropdown))
        driver.find_element_by_css_selector(data_dropdown).click()

        time.sleep(1)

        #Click on the downloads link
        downloads_link = ".popover-menu__link--downloads"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, downloads_link))
        driver.find_element_by_css_selector(downloads_link).click()

        time.sleep(1)

        #make sure you're on the data/downloads page
        self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//label[text()='Select export type']"))

        #make sure the submit button exists
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "input[type='submit']"))

        driver.find_element_by_css_selector("input[type='submit']").click()

        time.sleep(5)

        # Make sure the file was downloaded?
        if not self.does_file_exist_with_wildcard("/tmp/My_Awesome_Kobo_Form - *.xls*"):
            raise Exception("File was not downloaded")

if __name__ == "__main__":
    unittest.main()
