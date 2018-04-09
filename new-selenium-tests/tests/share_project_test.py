# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import empty_test
import time


class ShareProjectTest(empty_test.EmptyTest):

    def share_project(self):
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

            # switch to Form tab
            form_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Form']")
            ))
            form_tab_el.click()

            # click on the More Actions button
            more_actions_selector = "//a[contains(@data-tip,'More Actions')]"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, more_actions_selector))
            more_actions_el = driver.find_elements_by_xpath(more_actions_selector)
            more_actions_el[0].click()

            time.sleep(2)

            # click on the Share this Project button
            share_project_selector = "//a[text()='Share this project']"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, share_project_selector))
            clone_link = self.driver.find_elements_by_xpath(share_project_selector)
            clone_link[0].click()

            user_selector = "//input[@id='permsUser']"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, user_selector))
            driver.find_element_by_id("permsUser").clear()
            driver.find_element_by_id("permsUser").send_keys(self.username2)

            # Make sure the you are on the login page
            self.assertTrue(self.is_element_present_with_wait(By.ID, "id_username"))


            self.assertTrue(self.is_element_present(By.ID, "permsPassword"))
            driver.find_element_by_id("permsPassword").clear()
            driver.find_element_by_id("permsPassword").send_keys(self.password2)


            ok_button = self.driver.find_elements_by_css_selector(ok_selector)
            ok_button[0].click()


            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
