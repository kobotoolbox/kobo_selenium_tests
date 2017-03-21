# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import os
import glob
from time import sleep
import sys

class EmptyTest(unittest.TestCase):
    def setUp(self):
        #create a new browser session
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()

        #local env
        self.base_url = 'http://172.17.0.1:8000/'
        self.username = 'admin'
        self.password = 'admin'

        #test env
        # self.base_url = 'http://kf.kobotoolbox.org/'
        # self.username = 'selenium_test'
        # self.password = 'selenium_test'

        #production env
        # self.base_url = 'http://kf.kobotoolbox.org/'
        # self.username = 'selenium_test'
        # self.password = 'selenium_test'

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
        else: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def log_message(self, message):
        print self.log_prefix +" => "+ message

    def add_new_question(self, question_name, question_type, waiting_time=1):
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)
        #create a new empty question
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".survey-editor .btn--addrow"))
        el = driver.find_element_by_class_name("btn--addrow")
        self.mouse.move_to_element(el).click().perform()

        #Fill out the question's name
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, "form.row__questiontypes__form input"))
        question_title = driver.find_element_by_css_selector("form.row__questiontypes__form input[type='text']")
        question_title.send_keys(question_name)

        #Click on the add question button
        add_question_btn = driver.find_element(By.XPATH, '//button[text()=" + Add Question "]')
        add_question_btn.send_keys(Keys.ENTER)
        #make the question of type TEXT
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, ".questiontypelist__item[data-menu-item='"+question_type+"']"))
        first_input = driver.find_element_by_css_selector("div[data-menu-item='"+question_type+"']")
        self.mouse.move_to_element(first_input).click().perform()

        #wait for a little bit
        sleep(waiting_time)

    def delete_form(self):
        driver = self.driver
        self.mouse = webdriver.ActionChains(self.driver)

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
        sleep(2)

        #click on the Delete button
        delete_form_selector = ".popover-menu__link--delete"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, delete_form_selector))
        delete_form_btn = self.driver.find_elements_by_css_selector(delete_form_selector)
        delete_form_btn[0].click()

        sleep(2)

        #make sure the confirmation pop-up appears
        delete_btn = '//button[text()="Delete"]'
        self.assertTrue(self.is_element_present_with_wait(By.XPATH, delete_btn))

        try:
            delete_confirmation_checkboxes = driver.find_elements_by_css_selector(".alertify-toggle input[type='checkbox']")
            if len(delete_confirmation_checkboxes) > 0: #if this is a deployed form otherwise skip this step
                #check all the dialog's checkboxes
                for checkbox in delete_confirmation_checkboxes:
                    if not checkbox.get_attribute('checked'):
                        checkbox.click()
            driver.find_element_by_xpath(delete_btn).send_keys(Keys.ENTER)
        except :
            raise Exception("Couldn't delete the form")
        # except NoAlertPresentException:
        #     pass

    def generic_preview_form(self):
        driver = self.driver
        self.driver.get(self.base_url + "#/forms")
        self.mouse = webdriver.ActionChains(self.driver)
        #click on the form link
        form_link = ".asset-row__celllink"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
        form_link_el = driver.find_elements_by_css_selector(form_link)
        form_link_el[0].click()

        #click on the form preview link
        form_preview_link = ".form-view__link--preview"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_preview_link))
        preview_el = driver.find_elements_by_css_selector(form_preview_link)
        preview_el[0].click()


        #make sure the preview pop up showed up
        enketo_iframe = ".enketo-holder iframe"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, enketo_iframe))

        #return to the iframe
        driver.switch_to_frame(driver.find_element_by_css_selector(enketo_iframe))
        self.fill_out_enketo_form("#validate-form")

        #return to default frame
        driver.switch_to_default_content()

    def fill_out_enketo_form(self, validate_btn):
        #fill out name
        form_name_field = "input[name$='/Name']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_name_field))
        self.driver.find_element_by_css_selector(form_name_field).send_keys("Kobo")

        #fill out lastname
        form_name_field = "input[name$='/LastName']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_name_field))
        self.driver.find_element_by_css_selector(form_name_field).send_keys("Awesome")

        #fill out gender select-one field
        select_one_field = "input[name$='/Gender']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, select_one_field))
        select_el = self.driver.find_elements_by_css_selector(select_one_field)
        select_el[0].click()

        #fill out avatar
        form_name_field = "input[name$='/Avatar']"
        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_name_field))
        test_image = os.getcwd()+"/kobo-test-image.png"
        self.driver.find_element_by_css_selector(form_name_field).send_keys(test_image)

        self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, validate_btn))
        self.driver.find_element_by_css_selector(validate_btn).click()

        #Make sure the validation of the form submission is successful
        self.is_element_present_with_wait(By.CSS_SELECTOR, ".vex-dialog-message")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, '.vex-dialog-message.success'))

    @classmethod
    def does_file_exist_with_wildcard(self, filepath):
        for filepath_object in glob.glob(filepath):
            if os.path.isfile(filepath_object):
                return True
        return False


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
