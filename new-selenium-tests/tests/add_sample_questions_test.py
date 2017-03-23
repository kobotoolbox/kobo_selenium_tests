# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import empty_test

class AddSampleQuestionsTest(empty_test.EmptyTest):

    def add_questions_test(self):
        try :
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            #create a new empty question and wait for 3 seconds by default or add a 3rd parameter with value of seconds to wait | this function is a helper function from the empty_test class
            self.add_new_question("Name", "text")
            self.add_new_question("LastName", "text")
            self.add_new_question("Avatar", "image")
            self.add_new_question("Gender", "select_one")

            #click the save button
            save_btn_selector = ".formBuilder-header__button--save"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, save_btn_selector, 10))
            driver.find_element_by_css_selector(save_btn_selector).send_keys(Keys.ENTER)
            time.sleep(3)

            #close the modal
            close_btn_selector = ".formBuilder-header__close"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, close_btn_selector, 10))
            driver.find_element_by_css_selector(close_btn_selector).send_keys(Keys.ENTER)

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
