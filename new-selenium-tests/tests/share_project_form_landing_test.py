# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException # NoSuchElementException, TimeoutException

from logout_test import LogoutTest
from login_test import LoginTest

import unittest
import empty_test
import time


class ShareProjectFormLandingTest(empty_test.EmptyTest):

    @staticmethod
    def navigate_to_form_tab(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            # click into form summary page
            form_link = ".asset-row__celllink--titled"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            # form_link_el = driver.find_elements_by_css_selector(form_link)
            form_link_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, form_link)
            ))
            form_link_el.click()

            # switch to Form tab
            form_tab_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'form-view__tab') and text()='Form']")
            ))
            form_tab_el.click()
        except Exception as e:
            self.handle_test_exceptions(e)

    @staticmethod
    def share_this_project(self):
        # click on the More Actions button
        more_actions_selector = "//a[contains(@data-tip,'More Actions')]"
        self.assertTrue(self.is_element_present_with_wait(By.XPATH, more_actions_selector))
        more_actions_el = self.driver.find_elements_by_xpath(more_actions_selector)
        more_actions_el[0].click()

        time.sleep(2)

        # click on the Share this Project button
        share_project_selector = "//a[text()='Share this project']"
        self.assertTrue(self.is_element_present_with_wait(By.XPATH, share_project_selector))
        share_link = self.driver.find_elements_by_xpath(share_project_selector)
        share_link[0].click()

    @staticmethod
    def wait_for_correct_current_url(self, desired_url):
        self.driver.wait.until(
            lambda driver: driver.current_url == desired_url)

    def share_project_form_landing(self):
        try:
            ShareProjectFormLandingTest.navigate_to_form_tab(self)
            ShareProjectFormLandingTest.share_this_project(self)

            user_selector = "//input[@id='permsUser']"
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, user_selector))
            user_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, user_selector)
            ))
            user_el.clear()
            user_el.send_keys(self.username2)

            time.sleep(2)

            # Tab three times after entering the username
            user_el.send_keys(Keys.TAB + Keys.TAB + Keys.TAB)  # tab over to not-visible element

            share_by_link_checkbox_selector = "//input[@id='share-by-link']"

            share_by_link_checkbox_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, share_by_link_checkbox_selector)
            ))

            if not share_by_link_checkbox_el.is_selected():
                print "share_by_link_checkbox started out NOT selected"
                # The checkbox doesn't want to accept a click (It delivers an ElementNotVisibleException.)
                # But the SPACE key works.
                share_by_link_checkbox_el.send_keys(Keys.SPACE)
            else:
                print "share_by_link_checkbox is already selected; deselect; reselect."
                share_by_link_checkbox_el.send_keys(Keys.SPACE)
                time.sleep(1)
                share_by_link_checkbox_el.send_keys(Keys.SPACE)

            link_value_selector = "//div[@class='form-modal__item form-modal__item--shareable-link']//input[@type='text']"
            link_value_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, link_value_selector)
            ))
            if link_value_el.is_displayed():
                print link_value_el.get_attribute("value")
                link = link_value_el.get_attribute("value")

            # Click INVITE button
            invite_button_selector = "button.mdl-button.mdl-js-button"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, invite_button_selector))
            invite_button_el = self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, invite_button_selector)
            ))
            invite_button_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.XPATH,
                            "//div[@class='user-row__name'][contains(text(),'selenium_test_2')]", how_long=4)
                            )

            try:
                LogoutTest.do_logout(test_instance=self)
                LoginTest.do_login(test_instance=self, account_name='selenium_test_2')

            except Exception as e:
                self.handle_test_exceptions(e)

            time.sleep(3)
            self.assertTrue(self.is_element_present_with_wait(By.XPATH,
                                                              "//span[@class='asset-name'][contains(text(),'My Awesome KoboToolbox Form')]",  how_long=5))

            # Hover over the assets action buttons
            form_link = ".asset-row__buttons"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = self.driver.find_elements_by_css_selector(form_link)
            self.mouse.move_to_element(form_link_el[0]).move_by_offset(0, 1).perform()
            time.sleep(1)

            # Assert that the share button is not present in the selenium_test_2 account
            self.assertFalse(self.is_element_present_with_wait(By.CSS_SELECTOR,
                            ".asset-row__action-icon--sharing", how_long=3))
            ShareProjectFormLandingTest.navigate_to_form_tab(self)
            # We ensure thatthe page is going to the same link that was shared in the Sharing Permission, above
            ShareProjectFormLandingTest.wait_for_correct_current_url(self, link + "/landing")

            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//a[@data-tip='Editing capabilities not granted, you can only view this form']"))

            # Log out of the second account, and into the first
            try:
                LogoutTest.do_logout(test_instance=self)
                LoginTest.do_login(test_instance=self)
            except Exception as e:
                self.handle_test_exceptions(e)


            # ShareProjectFormLandingTest.navigate_to_form_tab(self)
            # # self.driver.wait.until(EC.url_to_be(link))
            # ShareProjectFormLandingTest.share_this_project(self)
            #
            # time.sleep(2)
            #
            # # Remove the shared account
            # trash_icon_selector = ".k-icon-trash"
            # self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, trash_icon_selector))
            # trash_icon_el = self.driver.wait.until(EC.presence_of_element_located(
            #     (By.CSS_SELECTOR, trash_icon_selector)
            # ))
            # trash_icon_el.click()
            #
            # # TODO: Deselect the share_by_link_checkbox
            #
            # close_record_detail_el = self.driver.wait.until(EC.presence_of_element_located(
            #     (By.XPATH, "//a[@class='modal-x']")
            # ))
            # close_record_detail_el.click()

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
