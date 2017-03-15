# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time

class DeployImportedFormTest(empty_test.EmptyTest):

    def deploy_form(self):
        self.log_prefix = "DeployImportedFormTest.deploy_form"
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        driver.get(self.base_url + "#/forms")

        #Hover over the assets action buttons
        form_link = ".asset-row__buttons"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_el = driver.find_elements_by_css_selector(form_link)
        self.mouse.move_to_element(form_link_el[0]).move_by_offset(0,1).perform()

        #click on the More Actions button
        more_actions_button = "button[data-tip='More Actions']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, more_actions_button))
        more_actions_el = driver.find_elements_by_css_selector(more_actions_button)
        more_actions_el[0].click()

        time.sleep(2)

        #click on the deploy button
        deploy_form_selector = ".popover-menu__link--deploy"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, deploy_form_selector))
        deploy_form_btn = self.driver.find_elements_by_css_selector(deploy_form_selector)
        deploy_form_btn[0].click()

        time.sleep(2)

        #make sure the status text exists
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".form-view__status span"))

        deployed = driver.find_element_by_css_selector(".form-view__status span > span").text
        self.log_message("DEPLOYED TEXT ======================" + deployed)
        if deployed != "Deployed":
            raise Exception("The imported form was not deployed")

if __name__ == "__main__":
    unittest.main()
