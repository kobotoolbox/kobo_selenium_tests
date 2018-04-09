# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import empty_test


class AddNewQuestionBlockTest(empty_test.EmptyTest):

    def add_new_question_block(self):
        try:
            driver = self.driver
            driver.wait = WebDriverWait(driver, 5)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/forms")

            # Enter My Library
            library_selector = ".library.k-drawer__link"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, library_selector))
            form_link_el = driver.find_elements_by_css_selector(library_selector)
            form_link_el[0].click()

            # start new library
            new_library_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'popover-menu__toggle') and text()='new']")
            ))
            new_library_el.click()

            # create new questions
            new_library_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'popover-menu__link') and text()='Question']")
            ))
            new_library_el.click()

            self.mouse = webdriver.ActionChains(self.driver)
            # create a new empty question and wait for one second by default
            # or add a third parameter with value of seconds to wait
            # this function is a helper function from the empty_test class
            self.add_new_question("Name", "text")
            self.add_new_question("LastName", "text")
            self.add_new_question("Avatar", "image")
            self.add_new_question("Gender", "select_one")

            # click the save button
            save_btn_selector = ".formBuilder-header__button--save"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, save_btn_selector, 10))
            driver.find_element_by_css_selector(save_btn_selector).send_keys(Keys.ENTER)
            time.sleep(2)
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//small[text()='and 3 other questions']"))

            # TODO: decide if we want to add this assertion,
            # since if it runs the very last second of the hour, it won't pass
            current_hour = int(time.strftime("%I"))
            time_phrase = "Today at {}')]".format(current_hour)
            time_xpath_string = "//span[contains(text(), '"+time_phrase
            print time_xpath_string
            self.assertTrue(self.is_element_present_with_wait(By.XPATH, time_xpath_string ))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
