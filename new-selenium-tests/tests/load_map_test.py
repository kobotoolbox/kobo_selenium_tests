# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import empty_test
from deploy_imported_form_test import DeployImportedFormTest


class LoadMapTest(empty_test.EmptyTest):

    def load_map(self):
        try:
            driver = self.driver
            self.mouse = webdriver.ActionChains(self.driver)
            time.sleep(5)
            map_container_selector = ".leaflet-container"
            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, map_container_selector))
            # map_pane_selector = '//'
            map_container_el = driver.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".leaflet-container")
            ))

            # self.mouse.move_to_element(map_container_el).move_by_offset(40, 25).click().perform()


            geodetect_btn_selector = "//button[@name = 'geodetect']"
            geodetect_btn_el = driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, geodetect_btn_selector)
            ))
            geodetect_btn_el.click()

            self.assertTrue(self.is_element_present_with_wait(By.CSS_SELECTOR, '.leaflet-marker-icon'))




            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
