# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import empty_test
import time
from selenium.common.exceptions import NoAlertPresentException


class AddQuestionBlockToCollectionTest(empty_test.EmptyTest):

    def add_question_block_to_collection(self):
        try:
            driver = self.driver
            driver.implicitly_wait(0)
            self.mouse = webdriver.ActionChains(self.driver)
            driver.get(self.base_url + "#/library")

            # click on the More Actions button
            more_actions_button = ".popover-menu--assetrow-menu"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, more_actions_button))
            more_actions_el = driver.find_elements_by_css_selector(more_actions_button)
            more_actions_el[0].click()

            #
            # # Hover over the more actions buttons
            # more_actions_selector = ".k-icon-more"
            # more_actions_el = driver.wait.until(EC.presence_of_element_located(
            #     (By.CSS_SELECTOR, more_actions_selector)
            # ))
            # more_actions_el.click()

            time.sleep(2)


            # https://stackoverflow.com/questions/9199415/getting-first-node-in-xpath-result-set
            move_to_selector = "(//*[@class='asset-row__buttons'])[1]/div/div/div[@class='popover-menu__moveTo']/div[@title='My Wonderful KoboToolbox Collection']"
            time.sleep(1)
            # Quick Check
            move_to_selector_el = driver.wait.until(EC.visibility_of_element_located(
                (By.XPATH, move_to_selector)
            ))
            move_to_selector_el.click()


            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
