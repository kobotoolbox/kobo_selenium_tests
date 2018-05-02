# -*- coding: utf-8 -*-
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
import unittest
import empty_test
import time


class ArchiveProjectTest(empty_test.EmptyTest):

    def archive_project(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
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

            # click on the Archive button
            archive_link_selector = ".popover-menu__link.popover-menu__link--archive"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, archive_link_selector))
            archive_link_el = self.driver.find_elements_by_css_selector(archive_link_selector)
            archive_link_el[0].click()

            archive_button_selector = ".ajs-button.ajs-ok"
            # delete_button = self.driver.find_elements_by_css_selector(ok_selector)
            archive_button_el = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, archive_button_selector)
            ))

            archive_button_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='archived project']"))

            form_link_selector = ".asset-row__celllink--titled"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link_selector))
            form_link_el = driver.find_elements_by_css_selector(form_link_selector)

            # TODO Why doesn't this work?
            # form_link_el = driver.wait.until(EC.presence_of_element_located(
            #    (By.CSS_SELECTOR, form_link_selector)
            # ))

            form_link_el[0].click()

            # switch to Form tab
            form_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Form']")
            ))
            form_tab_el.click()

            self.assertFalse(self.is_element_present_with_wait(By.XPATH, "//div[@class='form-view__cell form-view__cell--label'][contains(text(),'Collect data')]", how_long=3))

            unarchive_button_selector = "//a[@class='mdl-button mdl-button--raised mdl-button--colored']"
            # unarchive_button_sele /ctor = ".mdl-button--raised.mdl-button--colored"
            # delete_button = self.driver.find_elements_by_css_selector(ok_selector)
            unarchive_button_el = driver.wait.until(EC.visibility_of_element_located(
                (By.XPATH, unarchive_button_selector)
            ))
            unarchive_button_el.click()

            unarchive_button_confirm_selector = ".ajs-button.ajs-ok"
            # delete_button = self.driver.find_elements_by_css_selector(ok_selector)
            unarchive_button_confirm_el = driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, unarchive_button_confirm_selector)
            ))
            unarchive_button_confirm_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[@class='form-view__cell form-view__cell--label'][contains(text(),'Collect data')]"))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
