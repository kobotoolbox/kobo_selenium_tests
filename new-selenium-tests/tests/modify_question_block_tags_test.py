# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import empty_test
import time


class ModifyQuestionBlockTagsTest(empty_test.EmptyTest):

    def modify_question_block_tags(self):
        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")

            # Hover over the assets action buttons
            form_link = ".asset-row__buttons"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, form_link))
            form_link_el = driver.find_elements_by_css_selector(form_link)
            self.mouse.move_to_element(form_link_el[0]).move_by_offset(0, 1).perform()
            print "assertTrue asset-row__buttons and clicked"

            # click on the Tags button
            tag_button_selector = ".popover-menu--assetrow-menu"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, tag_button_selector))
            tag_button_el = driver.find_elements_by_css_selector(tag_button_selector)
            tag_button_el[0].click()

            time.sleep(1)

            # click on the Tags button
            tags_selector = "//a[@data-tip='Tags']"
            tag_btn_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, tags_selector)
            ))
            tag_btn_el.click()

            # self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//div[text()='deployed form']"))
            #
            # self.assertTrue(self.is_element_present_with_wait(By.XPATH, "//a[text()='redeploy']"))

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
