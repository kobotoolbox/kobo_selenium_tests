# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time

class EnketoFormSubmissionTest(empty_test.EmptyTest):

    def submit_from_enketo(self):
        self.log_prefix = "EnketoFormSubmissionTest.submit_from_enketo"
        self.log_message("Reached, Enketo Form Submission Test")
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")

        #Hover over the assets action buttons
        form_link = ".asset-row__celllink--titled"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_el = driver.find_elements_by_css_selector(form_link)
        form_link_el[0].click()

        #click on the More Actions button
        collection_option = "#collect-options"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, collection_option))
        more_actions_el = driver.find_elements_by_css_selector(collection_option)
        more_actions_el[0].click()

        time.sleep(2)

        #select enketo link
        enketo_popup_link = collection_option + " + .mdl-menu__container a:nth-child(2)"

        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, enketo_popup_link))
        enketo_online_link = self.driver.find_element_by_css_selector(enketo_popup_link)
        enketo_online_link.click()

        time.sleep(2)

        #click on the open button
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".open"))
        enketo_form_link = driver.find_element_by_css_selector(".open").get_attribute("href")

        driver.get(enketo_form_link)

        time.sleep(2)
        #make sure form title exiists
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "#form-title"))

        #submit in enketo
        self.fill_out_enketo_form("#submit-form")

if __name__ == "__main__":
    unittest.main()
