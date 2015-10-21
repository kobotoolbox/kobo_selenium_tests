# -*- coding: utf-8 -*-
import unittest
import time
import re

import requests
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class EnterDataTestEdited(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://kc.kbtdev.org/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_enter_data_test_edited(self):
        driver = self.driver
        driver.get(self.base_url + "")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Selenium test form title."))
        project_url= driver.find_elements_by_link_text("Selenium test form title.")[0].get_attribute("href")
        driver.find_element_by_link_text("Selenium test form title.").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, ".dashboard__button-enter-data"):
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        data_entry_url = driver.find_element_by_css_selector(
            ".dashboard__button-enter-data").get_attribute("href")
        # WARNING: The 'open' command doesn't export correctly to Python, always
        # behaving as if a relative address has been provided, so a manual edit is
        # necessary.
        driver.get(data_entry_url)
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "form-title"):
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        self.assertEqual(
            "Selenium test form title.", driver.find_element_by_css_selector("#form-title").text)
        self.assertEqual(
            "Selenium test question label.", driver.find_element_by_css_selector(".question-label").text)
        self.assertEqual("Selenium test question choice 1.", driver.find_element_by_css_selector(
            ".question label:nth-child(1) .option-label").text)
        self.assertEqual("Selenium test question choice 2.", driver.find_element_by_css_selector(
            ".question label:nth-child(2) .option-label").text)
        driver.find_element_by_css_selector(".question label:nth-child(1)").click()
        if self.enketo_express:
            submission_queue_selector= '.offline-enabled__queue-length'
        else:
            submission_queue_selector= '.queue-length'
        for i in range(60):
            try:
                if "0" == driver.find_element_by_css_selector(submission_queue_selector).text:
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        self.assertTrue(self.is_element_present(By.ID, "submit-form"))
        driver.find_element_by_id("submit-form").click()
        # Ensure that the data was submitted and no alerts were generated.
        for i in range(60):
            try:
                if "1" == driver.find_element_by_css_selector(submission_queue_selector).text:
                    break
            except:
                pass
            # This is a momentary occurrence, so try hard to catch it.
            # time.sleep(1)
        else:
            self.fail("time out")
        if self.enketo_express:
            # FIXME: We consistently timeout waiting for Enketo to clear its queue; find the cause.
            submission_queue_timeout= 300
        else:
            submission_queue_timeout= 60
        for i in range(submission_queue_timeout):
            try:
                if "0" == driver.find_element_by_css_selector(submission_queue_selector).text:
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        if not self.enketo_express:
            self.assertEqual(
                "", driver.find_element_by_css_selector("#dialog-alert .modal-header").text)
        driver.get(self.base_url + self.KOBO_USERNAME + "/forms/Selenium_test_form_title")
        # Close out the "unsaved changes" warning.
        if (not self.enketo_express) and self.is_alert_present():
            driver.switch_to_alert().accept()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, ".dashboard__submissions .dashboard__group-label"):
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        self.assertEqual("Submissions (1)", driver.find_element_by_css_selector(
            ".dashboard__submissions .dashboard__group-label").text)

        # Verify that the QR code image is present.
        driver.find_element_by_css_selector(".dashboard__button-how-to-collect").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, ".vex-content .qrcode__code img.qrcode"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        # Verify that the QR code is retrievable.
        response= requests.get(project_url + '/qrcode', allow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
