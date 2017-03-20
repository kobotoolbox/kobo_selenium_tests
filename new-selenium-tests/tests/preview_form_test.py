# -*- coding: utf-8 -*-
import unittest
import empty_test

class PreviewFormTest(empty_test.EmptyTest):

    def preview_form(self):
        self.log_prefix = "PreviewFormTest.preview_form"
        self.log_message("Reached, Preview form Test")

        #This is an empty_test method!
        self.generic_preview_form()

if __name__ == "__main__":
    unittest.main()
