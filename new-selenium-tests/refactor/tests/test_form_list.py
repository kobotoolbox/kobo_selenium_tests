# -*- coding: utf-8 -*-

import unittest
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..settings import BASE_URL
from .test_authentication import AuthenticatedUserTestCase

MAX_FORM_DELETIONS = 10


class FormListTests(AuthenticatedUserTestCase):

    def delete_first_asset(self):
        self.driver.get(BASE_URL + "#/forms")
        self.mouse = webdriver.ActionChains(self.driver)

        # Hover over the assets action buttons
        form_link = ".asset-row__buttons"
        try:
            self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, form_link)
            ))
        except TimeoutException:
            return False
        form_link_el = self.driver.find_elements_by_css_selector(form_link)
        self.mouse.move_to_element(form_link_el[0]).perform()

        # click on the More Actions button
        more_actions_button = ".popover-menu--assetrow-menu"
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, more_actions_button)
        ))
        more_actions_el = self.driver.find_elements_by_css_selector(more_actions_button)
        more_actions_el[0].click()
        sleep(0.5)

        # click on the Delete button
        delete_form_selector = ".popover-menu__link--delete"
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, delete_form_selector)
        ))
        delete_form_button = self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, delete_form_selector)
        ))
        delete_form_button.click()
        sleep(0.5)

        # make sure the confirmation pop-up appears
        delete_btn = '//button[text()="Delete"]'
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, delete_btn)
        ))

        while True:
            delete_confirmation_labels = self.driver.find_elements_by_css_selector(
                '.alertify-toggle input[type="checkbox"]:not(:checked)'
            )
            if not delete_confirmation_labels:
                break
            # Checkbox itself is not visible, so click the parent
            delete_confirmation_labels[0].find_element_by_xpath('..').click()

        self.driver.find_element_by_xpath(delete_btn).send_keys(Keys.ENTER)
        # self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='project deleted permanently']"))
        return True

    def start_new_project(self, name):
        # when /#/forms is devoid of forms, the “NEW” button is accessed the 'button' selector.
        # And when there is a form already created, the same button is accessed via the 'a..'selector
        new_btn_selector = "//a[contains(@class, 'popover-menu__toggle') and text()='new']"
        new_button_el = self.driver.find_elements_by_xpath(new_btn_selector)
        if len(new_button_el) > 0 and new_button_el[0].is_displayed():
            new_button_el[0].click()
            print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
        else:
            new_btn_selector = "//button[contains(@class, 'mdl-button--raised') and text()='new']"
            new_button_el = self.driver.find_elements_by_xpath(new_btn_selector)
            new_button_el[0].click()
            print ("Button")

            self.driver.wait.until(EC.presence_of_element_located(
                (By.ID, "name")
            ))
            self.driver.find_element_by_css_selector("#name").send_keys(name)

            # fill form description
            description_selector = ".form-modal__item:nth-child(2) textarea"
            self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, description_selector)
            ))
            self.driver.find_element_by_css_selector(description_selector).send_keys("My form's description")

            # select form sector
            sector_input = ".form-modal__item--sector .Select-input input"
            self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, sector_input)
            ))
            sector_el = self.driver.find_element_by_css_selector(sector_input)
            sector_el.send_keys("Public Administration")
            sector_el.send_keys(Keys.ENTER)

            # fill country input
            country_input = ".form-modal__item--country .Select-input input"
            self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, country_input)
            ))
            country_el = self.driver.find_element_by_css_selector(country_input)
            country_el.send_keys("United States")
            country_el.send_keys(Keys.ENTER)

            self.driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".form-modal__item--actions button")
            ))
            submit_button = self.driver.find_element(By.CSS_SELECTOR, ".form-modal__item--actions button")
            submit_button.send_keys(Keys.ENTER)

    def test_delete_all_forms(self):
        deletions = 0
        while deletions < MAX_FORM_DELETIONS:
            if not self.delete_first_asset():
                break
            # TODO: it would be better to make sure that the deleted form
            # has actually disappeared from the form list before calling
            # `delete_form()` again, since there's a bit of a delay between
            # confirming the deletion and the list of forms refreshing
            sleep(2)
        deletions += 1

    def test_verify_no_forms(self):
        self.driver.get(BASE_URL + "#/forms")
        form_submissions = self.driver.find_elements_by_css_selector(
            '.asset-row__celllink'
        )
        self.assertEqual(len(form_submissions), 0)

    def test_create_new_form_from_scratch(self, delete_afterwards=True):
        # go to new form page and click on the sidebar menu
        self.driver.get(BASE_URL + "#/forms")

        self.start_new_project("My Awesome KoboToolbox Form")

        # Complete "Create New Project (step 2 of 2)"
        design_button_el = self.driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[text() = 'Design in Form Builder']")
        ))
        design_button_el.click()
        self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".formBuilder")
        ))
        if delete_afterwards:
            self.test_delete_all_forms()

    def test_deploy_form(self, delete_afterwards=True):
        self.test_create_new_form_from_scratch(delete_afterwards=False)

        self.driver.get(BASE_URL + "#/forms")
        mouse = webdriver.ActionChains(self.driver)

        # Hover over the assets action buttons
        form_link = ".asset-row__buttons"
        self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, form_link)
        ))
        form_link_el = self.driver.find_elements_by_css_selector(form_link)
        mouse.move_to_element(form_link_el[0]).move_by_offset(0, 1).perform()

        # click on the More Actions button
        more_actions_button = ".popover-menu--assetrow-menu"
        self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, more_actions_button)
        ))
        more_actions_el = self.driver.find_elements_by_css_selector(more_actions_button)
        more_actions_el[0].click()

        sleep(1)

        # click on the deploy menu item
        deploy_form_selector = ".popover-menu__link--deploy"
        self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, deploy_form_selector)
        ))
        # deploy_form_btn = self.driver.find_elements_by_css_selector(deploy_form_selector)
        deploy_form_btn_el = self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, deploy_form_selector)
        ))
        deploy_form_btn_el.click()

        self.driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[text()='deployed form']")
        ))

        self.driver.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//a[text()='redeploy']")
        ))

        if delete_afterwards:
            self.test_delete_all_forms()

    def test_export_form_to_xls(self, delete_afterwards=True):
        self.test_create_new_form_from_scratch(delete_afterwards=False)

        mouse = webdriver.ActionChains(self.driver)
        self.driver.get(BASE_URL + "#/forms")

        # Hover over the assets action buttons
        form_link = ".asset-row__buttons"
        self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, form_link)
        ))
        form_link_el = self.driver.find_elements_by_css_selector(form_link)
        mouse.move_to_element(form_link_el[0]).move_by_offset(0, 1).perform()
        sleep(1)

        # click on the More Actions button
        more_actions_button = ".popover-menu--assetrow-menu"
        self.driver.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, more_actions_button)
        ))
        more_actions_el = self.driver.find_elements_by_css_selector(more_actions_button)
        more_actions_el[0].click()

        sleep(1)

        # click on the Download as XLS button
        xls_link_selector = ".popover-menu__link.popover-menu__link--dl-xls"
        xls_link_el = self.driver.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, xls_link_selector)
        ))
        xls_link_el.click()

        # TODO: verify the downloaded file?

        if delete_afterwards:
            self.test_delete_all_forms()
