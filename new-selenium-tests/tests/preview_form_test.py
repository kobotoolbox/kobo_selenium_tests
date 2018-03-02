# -*- coding: utf-8 -*-
import unittest
import empty_test


class PreviewFormTest(empty_test.EmptyTest):

    def preview_form(self):
        try:
            # This is an empty_test method!
            self.generic_preview_form()

            self.status("PASSED")

        except Exception as e:
            self.handle_test_exceptions(e)


if __name__ == "__main__":
    unittest.main()
