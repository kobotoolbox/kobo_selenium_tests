# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import unittest
import os
import glob
from time import sleep
import sys
import inspect
import traceback


class EmptyTest(unittest.TestCase):
    def setUp(self):
        # create a new browser session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()

        # local env
        self.base_url = ''
        self.username = ''
        self.password = ''
        self.verificationErrors = []
        self.accept_next_alert = True
        self.log_prefix = "Empty"
        self.mouse = webdriver.ActionChains(self.driver)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_element_present_with_wait(self, how, what, how_long=60):
        # message = "Looking for: " +how+ " for: " + what
        for i in range(how_long):
            # print message +  " [time: "+`i + 1`+" of "+`how_long + 1`+"]"
            if self.is_element_present(how, what):
                break
            sleep(1)
        else:
            return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException, e:
            return False
        return True


    def startNewProject(self, name):
        driver = self.driver

        # when /#/forms is devoid of forms, the “NEW” button is accessed the 'button' selector.
        # And when there is a form already created, the same button is accessed via the 'a..'selector
        new_btn_selector = "//a[contains(@class, 'popover-menu__toggle') and text()='new']"
        new_button_el = driver.find_elements_by_xpath(new_btn_selector)
        if len(new_button_el) > 0 and new_button_el[0].is_displayed():
            new_button_el[0].click()
            print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
        else:
            new_btn_selector = "//button[contains(@class, 'mdl-button--raised') and text()='new']"
            new_button_el = driver.find_elements_by_xpath(new_btn_selector)
            new_button_el[0].click()
            print ("Button")

            self.assertTrue(self.is_element_present_with_wait(By.ID, "name"))
            driver.find_element_by_css_selector("#name").send_keys(name)

            # fill form description
            description_selector = ".form-modal__item:nth-child(2) textarea"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, description_selector))
            driver.find_element_by_css_selector(description_selector).send_keys("My form's description")

            # select form sector
            sector_input = ".form-modal__item--sector .Select-input input"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, sector_input))
            sector_el = driver.find_element_by_css_selector(sector_input)
            sector_el.send_keys("Public Administration")
            sector_el.send_keys(Keys.ENTER)

            # fill country input
            country_input = ".form-modal__item--country .Select-input input"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, country_input))
            country_el = driver.find_element_by_css_selector(country_input)
            country_el.send_keys("United States")
            country_el.send_keys(Keys.ENTER)

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".form-modal__item--actions button"))
            submit_button = driver.find_element(By.CSS_SELECTOR, ".form-modal__item--actions button")
            submit_button.send_keys(Keys.ENTER)



    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def add_new_question(self, question_name, question_type, waiting_time=2):
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        # create a new empty question
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".survey-editor .btn--addrow"))
        el = driver.find_element_by_class_name("btn--addrow")
        self.mouse.move_to_element(el).click().perform()

        # Fill out the question's name
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "form.row__questiontypes__form input"))
        question_title = driver.find_element_by_css_selector("form.row__questiontypes__form input[type='text']")
        question_title.send_keys(question_name)

        # Click on the add question button
        add_question_btn = driver.find_element(By.XPATH, '//button[text()=" + Add Question "]')
        add_question_btn.send_keys(Keys.ENTER)
        # make the question of type TEXT
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".questiontypelist__item[data-menu-item='"+question_type+"']"))
        first_input = driver.find_element_by_css_selector("div[data-menu-item='"+question_type+"']")
        self.mouse.move_to_element(first_input).click().perform()

        # wait for a little bit
        sleep(waiting_time)

    def delete_form(self):
        driver = self.driver
        driver.wait = WebDriverWait(driver, 5)
        self.mouse = webdriver.ActionChains(self.driver)

        # Hover over the assets action buttons
        form_link = ".asset-row__buttons"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_el = driver.find_elements_by_css_selector(form_link)
        self.mouse.move_to_element(form_link_el[0]).perform()

        # click on the More Actions button
        more_actions_button = ".popover-menu--assetrow-menu"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, more_actions_button))
        more_actions_el = driver.find_elements_by_css_selector(more_actions_button)
        more_actions_el[0].click()
        sleep(0.5)

        # click on the Delete button
        delete_form_selector = ".popover-menu__link--delete"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, delete_form_selector))
        delete_form_button = driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, delete_form_selector)
            ))
        delete_form_button.click()

        sleep(0.5)

        # make sure the confirmation pop-up appears
        delete_btn = '//button[text()="Delete"]'
        self.assertTrue(self.is_element_present_with_wait(By.XPATH, delete_btn))

        try:
            delete_confirmation_labels = driver.find_elements_by_css_selector(".alertify-toggle label")
            if len(delete_confirmation_labels) > 0:  # if this is a deployed form otherwise skip this step
                # check all the dialog's checkboxes
                for checkbox in delete_confirmation_labels:
                    # if not checkbox.get_attribute('checked'):
                    checkbox.click()

            driver.find_element_by_xpath(delete_btn).send_keys(Keys.ENTER)
            # self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='project deleted permanently']"))
            sleep(1)
        except:
            raise Exception("Couldn't delete the form")
        # except NoAlertPresentException:
        #     pass

    def generic_preview_form(self):
        driver = self.driver
        self.driver.get(self.base_url + "#/forms")
        self.mouse = webdriver.ActionChains(self.driver)
        # click on the form link
        form_link = ".asset-row__celllink"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_el = driver.find_elements_by_css_selector(form_link)
        form_link_el[0].click()
        print "Clicked asset-row__celllink"

        # click on the form preview link
        form_preview_link = ".form-view__link--preview"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_preview_link))
        preview_el = driver.find_elements_by_css_selector(form_preview_link)
        preview_el[0].click()
        print "Clicked form-view__link--preview"

        # make sure the preview pop up showed up
        enketo_iframe = ".enketo-holder iframe"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, enketo_iframe))
        print "EXIST CHECKED: enketo-holder iframe "
        # return to the iframe
        driver.switch_to.frame(driver.find_element_by_css_selector(enketo_iframe))
        self.fill_out_enketo_form("#validate-form")
        print "validate-form"
        # return to default frame
        driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(".modal-x").click()

    def fill_out_enketo_form(self, validate_btn):
        # driver = self.driver
        self.driver.wait = WebDriverWait(self.driver, 5)
        # fill out name
        form_name_field = "input[name$='/Name']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_name_field))
        # self.driver.find_element_by_css_selector(form_name_field).send_keys("Kobo")
        self.driver.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, form_name_field)
            )).send_keys("Kobo")
        # fill out lastname
        form_name_field = "input[name$='/LastName']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_name_field))
        self.driver.find_element_by_css_selector(form_name_field).send_keys("Awesome")

        # fill out gender select-one field
        select_one_field = "input[name$='/Gender']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, select_one_field))
        select_el = self.driver.find_elements_by_css_selector(select_one_field)
        select_el[0].click()

        # fill out avatar
        form_name_field = "input[name$='/Avatar']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_name_field))
        test_image = os.getcwd()+"/kobo-test-image.png"
        self.driver.find_element_by_css_selector(form_name_field).send_keys(test_image)




        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, validate_btn))
        self.driver.find_element_by_css_selector(validate_btn).click()

        # Make sure the validation of the form submission is successful
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".vex-dialog-message"))
        if not self.is_element_present_with_wait(By.CSS_SELECTOR, ".vex-dialog-message.success"):
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, '.vex-dialog-message.success'))

    @classmethod
    def status(cls, status):
        print status + ": " + sys._getframe().f_back.f_code.co_name

    @classmethod
    def handle_test_exceptions(cls, e):
        print "FAILED: " + sys._getframe().f_back.f_code.co_name
        print "An Exception of type " + str(type(e)) +\
              " happened while trying to create a "+sys._getframe().f_back.f_code.co_name+" more info: "
        print "Arguments: " + str(e.args)
        print "Message: " + e.message
        traceback.print_exc()
        raise e

    @classmethod
    def does_file_exist_with_wildcard(cls, filepath):
        for filepath_object in glob.glob(filepath):
            if os.path.isfile(filepath_object):
                return True
        return False

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    @staticmethod
    def navigate_to_main_page(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

        except Exception as e:
            self.handle_test_exceptions(e)

if __name__ == "__main__":
    unittest.main()
