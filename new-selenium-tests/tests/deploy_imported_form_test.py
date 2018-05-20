# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import empty_test
import time


class DeployImportedFormTest(empty_test.EmptyTest):

    def deploy_form(self):
        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            # Hover over the assets action buttons
            form_link = ".asset-row__buttons"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = driver.find_elements_by_css_selector(form_link)
            self.mouse.move_to_element(form_link_el[0]).move_by_offset(0, 1).perform()

            # click on the More Actions button
            more_actions_button = ".popover-menu--assetrow-menu"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, more_actions_button))
            more_actions_el = driver.find_elements_by_css_selector(more_actions_button)
            more_actions_el[0].click()

            time.sleep(1)

            # click on the deploy button
            deploy_form_selector = ".popover-menu__link--deploy"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, deploy_form_selector))
            # deploy_form_btn = self.driver.find_elements_by_css_selector(deploy_form_selector)
            deploy_form_btn_el = driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, deploy_form_selector)
            ))
            deploy_form_btn_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='deployed form']"))

            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//a[text()='redeploy']"))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
