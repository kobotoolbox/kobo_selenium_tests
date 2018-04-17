import unittest
import os
import sys
import config
import time
import logging
from selenium import webdriver
from tests import empty_test
from tests import login_test
from tests import new_form_from_scratch_test
from tests import add_sample_questions_test
from tests import preview_form_test
from tests import delete_all_forms_test
from tests import import_xls_form_test
from tests import export_form_to_xls_test
from tests import deploy_imported_form_test
from tests import enketo_form_submission_test
from tests import custom_reports_test
from tests import view_table_record_test
from tests import clone_project_test
from tests import share_project_test
from tests import create_new_collection_test
from tests import add_new_question_block_test
from tests import add_question_block_to_collection_test
from tests import delete_collection_test
from tests import modify_question_block_tags_test
from tests import subscribe_library_collection_test
from tests import delete_library_block_test
from tests import export_data_to_xls_test
from tests import verify_no_forms_test
from tests import logout_test


# Inherit some helper functions automatically generated by Selenium IDE.
class Test_Selenium(empty_test.EmptyTest):
    # TODO: Remove? Unused?
    DEFAULT_WAIT_SECONDS = 10
    MAX_SUITE_TIME_MINUTES = 10
    timed_out = False
    # Get settings overrides from the environment.
    KOBOFORM_URL = os.environ.get('KOBOFORM_URL', 'https://kf.kobotoolbox.org/')
    if KOBOFORM_URL[-1] != '/':
        KOBOFORM_URL += '/'
    # TODO: Remove? Unused?
    KOBOCAT_URL = os.environ.get('KOBOCAT_URL', 'https://kc.kobotoolbox.org')
    if KOBOCAT_URL[-1] != '/':
        KOBOCAT_URL += '/'
    KOBO_USERNAME = os.environ.get('KOBO_USERNAME', 'selenium_test')
    KOBO_PASSWORD = os.environ.get('KOBO_PASSWORD', 'selenium_test')
    KOBO_USERNAME2 = os.environ.get('KOBO_USERNAME1', 'selenium_test2')
    KOBO_PASSWORD2 = os.environ.get('KOBO_PASSWORD1', 'selenium_test2')

    # TODO: Type is `str` or `bool`. Fix?
    KOBO_DISABLE_TIMEOUT = os.environ.get('KOBO_DISABLE_TIMEOUT', False)
    # TODO: Remove? Unused?
    ENKETO_VERSION = os.environ.get('ENKETO_VERSION', 'legacy')
    # TODO: Remove? Unused?
    assert ENKETO_VERSION.lower() in ['legacy', 'express']
    # TODO: Remove? Unused?
    enketo_express = ENKETO_VERSION.lower() == 'express'

    # Browser Constants
    BROWSER_WIDTH = 1500
    BROWSER_HEIGHT = 900
    BROWSER_IMPLICIT_WAIT = 0
    # TODO: Type is `str` or `int`. Fix?
    BROWSER_VISIBLE = os.environ.get('SELENIUM_BROWSER_VISIBLITY', 1)

    # chrome options:
    BROWSER_CHROME_OPTIONS = webdriver.ChromeOptions()
    BROWSER_CHROME_OPTIONS.add_experimental_option("prefs",
                                                   {"download.default_directory": "/tmp",
                                                    "download.prompt_for_download": False
                                                    })

    def check_timeout(self, status_message=''):
        if self.KOBO_DISABLE_TIMEOUT:
            return

        minutes_elapsed = (time.time() - self.suite_start_time) / 60
        if minutes_elapsed >= self.MAX_SUITE_TIME_MINUTES:
            # TODO: Remove? Unused?
            self.timed_out = True
            raise Exception('Test suite timed out: ' + status_message)

    # Don't use the inherited, automatically-generated setup and teardown methods.
    def setUp(self):
        self.check_timeout()

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        # http://stackoverflow.com/a/15400334/1877326
        # Disable debug logging.
        selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
        # Only display possible problems
        selenium_logger.setLevel(logging.WARN)

        if os.environ.get('SELENIUM_REMOTE_WEBDRIVER_ROOT'):
            # Use a remote Selenium Webdriver instance.
            remote_webdriver_root = os.environ['SELENIUM_REMOTE_WEBDRIVER_ROOT'].rstrip('/')
            cls.driver = webdriver.Remote(remote_webdriver_root + '/wd/hub',
                                          desired_capabilities=cls.BROWSER_CHROME_OPTIONS.to_capabilities())
        else:
            # jnm: This seems to require a package called xephyr, which I don't
            # want to bother with finding and installing.
            # TODO: Use headless Chrome when a browser window is not desired:
            # https://intoli.com/blog/running-selenium-with-headless-chrome/
            # Initialize a ghost Browser window set visible to 1 if you want to view the test as it runs
            # from pyvirtualdisplay import Display
            # cls.display = Display(visible=cls.BROWSER_VISIBLE, size=(cls.BROWSER_WIDTH, cls.BROWSER_HEIGHT))
            # cls.display.start()
            # Chrome set up
            cls.driver = webdriver.Chrome(chrome_options=cls.BROWSER_CHROME_OPTIONS)

        cls.driver.set_window_size(cls.BROWSER_WIDTH, cls.BROWSER_HEIGHT)
        cls.driver.implicitly_wait(cls.BROWSER_IMPLICIT_WAIT)
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.suite_start_time = time.time()

    @classmethod
    def find_xls_filenames(cls, path_to_dir, suffix=".xls"):  # was self
        filenames = os.listdir(path_to_dir)
        return [filename for filename in filenames if filename.endswith(suffix)]

    @classmethod
    def clear_xls_files(cls):  # was self
        tmp_directory = "/tmp"
        for fname in os.listdir(tmp_directory):
            if fname.endswith(".xls"):
                os.remove(os.path.join(tmp_directory, fname))

    @classmethod
    def tearDownClass(cls):
        # Clean up the downloaded XLS file if the test got that far.
        cls.clear_xls_files()

        # quit browser instance
        # cls.driver.quit()
        # quit the window
        # if isinstance(cls.driver, webdriver.Chrome):
        #    cls.display.stop()

    ALL_TESTS = {
        'test_101_login': {
            'test_class': login_test.LoginTest,
            'test_method': 'test_login'
        },
        'test_102_delete_all_forms': {
            'test_class': delete_all_forms_test.DeleteAllFormsTest,
            'test_method': 'delete_all_forms'
        },

        'test_103_new_form': {
            'test_class': new_form_from_scratch_test.NewFormFromScratchTest,
            'test_method': 'create_new_form_from_scratch'
        },
        'test_104_add_sample_question': {
            'test_class': add_sample_questions_test.AddSampleQuestionsTest,
            'test_method': 'add_questions_test'
        },
        'test_108_deploy_form': {
            'test_class': deploy_imported_form_test.DeployImportedFormTest,
            'test_method': 'deploy_form'
        },
        'test_109_submit_from_enketo': {
            'test_class': enketo_form_submission_test.EnketoFormSubmissionTest,
            'test_method': 'submit_from_enketo'
        },


        'test_110_custom_reports': {
            'test_class': custom_reports_test.CustomReports,
            'test_method': 'custom_reports'
        },

        'test_111_view_table_record': {
            'test_class': view_table_record_test.ViewTableRecordTest,
            'test_method': 'view_table_record'
        },

        # 'test_112_share_project': {
        #     'test_class': share_project_test.ShareProjectTest,
        #     'test_method': 'share_project'
        # },

        'test_113_clone_project': {
            'test_class': clone_project_test.CloneProjectTest,
            'test_method': 'clone_project'
        },
        'test_114_add_new_question_block': {
            'test_class': add_new_question_block_test.AddNewQuestionBlockTest,
            'test_method': 'add_new_question_block'
        },
        'test_115_create_new_collection': {
            'test_class': create_new_collection_test.CreateNewCollectionTest,
            'test_method': 'create_new_collection'
        },
        'test_116_add_question_block_to_collection': {
            'test_class': add_question_block_to_collection_test.AddQuestionBlockToCollectionTest,
            'test_method': 'add_question_block_to_collection'
        },

        'test_117_delete_collection': {
            'test_class': delete_collection_test.DeleteCollectionTest,
            'test_method': 'delete_collection'
        },

        'test_118_modify_question_block_tags': {
            'test_class': modify_question_block_tags_test.ModifyQuestionBlockTagsTest,
            'test_method': 'modify_question_block_tags'
        },
        'test_119_subscribe_library_collection': {
            'test_class': subscribe_library_collection_test.SubscribeLibraryCollectionTest,
            'test_method': 'subscribe_library_collection'
        },
        'test_120_delete_library_block': {
            'test_class': delete_library_block_test.DeleteLibraryBlockTest,
            'test_method': 'delete_library_block'
        },


        'test_220_delete_all_forms': {
            'test_class': delete_all_forms_test.DeleteAllFormsTest,
            'test_method': 'delete_all_forms'
        },
        'test_221_test_verify_no_forms': {
            'test_class': verify_no_forms_test.VerifyNoFormsTest,
            'test_method': 'test_verify_no_forms'
        },
        'test_222_test_logout': {
            'test_class': logout_test.LogoutTest,
            'test_method': 'test_logout'
        }
    }

    # Run all the tests based on the values from ALL_TESTS
    def test_step_00_run_all(self):
        self.base_url = self.KOBOFORM_URL
        # self.username = ""
        self.username = self.KOBO_USERNAME
        self.password = self.KOBO_PASSWORD
        self.username2 = self.KOBO_USERNAME2
        self.password2 = self.KOBO_PASSWORD2
        first_try = True
        # Run all the tests twice in case of a failure
        try:
            print "<============ 1st SELENIUM TEST TRY ============>"
            for key, current_test in sorted(self.ALL_TESTS.iteritems()):
                print "Reached: " + current_test.get('test_method')
                test_case_class = current_test.get('test_class')
                test_case_class.__dict__[current_test.get('test_method')](self)
        except:
            # TODO: Move second attempt out of the class and into `__main__`.
            # Initialize a new browser for a fresh test
            self.tearDownClass()
            self.setUpClass()
            print "<============ 2nd SELENIUM TEST TRY ============>"
            if first_try is True:
                for key, current_test in sorted(self.ALL_TESTS.iteritems()):
                    print "Reached: " + current_test.get('test_method')
                    test_case_class = current_test.get('test_class')
                    test_case_class.__dict__[current_test.get('test_method')](self)

                # raise


if __name__ == "__main__":
    unittest.main()
