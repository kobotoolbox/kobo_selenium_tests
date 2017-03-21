import unittest
import os
import sys
import config
import time
import logging
from pyvirtualdisplay import Display
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
from tests import export_data_to_xls_test
from tests import verify_no_forms_test
from tests import delete_form_test
from tests import logout_test

# Inherit some helper functions automatically generated by Selenium IDE.
class Test_Selenium(empty_test.EmptyTest):
    ENV_TYPE = 'local'
    DEFAULT_WAIT_SECONDS= 10
    MAX_SUITE_TIME_MINUTES= 10
    timed_out= False

    # Get settings overrides from the environment.
    KOBOFORM_URL= os.environ.get('KOBOFORM_URL', 'http://172.17.0.1:8000/')
    # KOBOFORM_URL= os.environ.get('KOBOFORM_URL', 'http://kf.kobotoolbox.org/')
    if KOBOFORM_URL[-1] != '/':
        KOBOFORM_URL+= '/'
    KOBOCAT_URL= os.environ.get('KOBOCAT_URL', 'http://172.17.0.1:8000/')
    if KOBOCAT_URL[-1] != '/':
        KOBOCAT_URL+= '/'
    KOBO_USERNAME= os.environ.get('KOBO_USERNAME', 'admin')
    KOBO_PASSWORD= os.environ.get('KOBO_PASSWORD', 'admin')
    KOBO_DISABLE_TIMEOUT= os.environ.get('KOBO_DISABLE_TIMEOUT', False)
    ENKETO_VERSION= os.environ.get('ENKETO_VERSION', 'legacy')
    assert ENKETO_VERSION.lower() in ['legacy', 'express']
    enketo_express= ENKETO_VERSION.lower() == 'express'


    def check_timeout(self, status_message=''):
        if self.KOBO_DISABLE_TIMEOUT:
            return

        minutes_elapsed= (time.time() - self.suite_start_time) / 60
        if minutes_elapsed >= self.MAX_SUITE_TIME_MINUTES:
            self.timed_out= True
            raise Exception('Test suite timed out: ' + status_message)

    # Don't use the inherited, automatically-generated setup and teardown methods.
    def setUp(self):
        print "INITIAL SET UP 2"
        print self.ENV_TYPE
        self.check_timeout()

    def tearDown(self):
        pass


    @classmethod
    def setUpClass(cls):
        print "INITIAL SET UP 1"
        print cls.ENV_TYPE
        # http://stackoverflow.com/a/15400334/1877326
        # Disable debug logging.
        selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
        # Only display possible problems
        selenium_logger.setLevel(logging.WARN)

        #Initialize a ghost Browser window set visible to 1 if you want to view the test as it runs
        cls.display = Display(visible=1, size=(1500, 1200))
        cls.display.start()

        #Chrome set up
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "/tmp", "download.prompt_for_download": False})
        cls.driver = webdriver.Chrome(chrome_options=chromeOptions)
        cls.driver.implicitly_wait(0)
        cls.driver.set_window_size(1500, 1200)
        cls.driver.maximize_window()

        cls.driver.implicitly_wait(0)
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.suite_start_time= time.time()
        cls.tmp_file_before = cls.find_xls_filenames("/tmp")

    @classmethod
    def find_xls_filenames(self, path_to_dir, suffix=".xls" ):
        filenames = os.listdir(path_to_dir)
        return [ filename for filename in filenames if filename.endswith( suffix ) ]


    @classmethod
    def tearDownClass(cls):
        # Clean up the downloaded XLS file if the test got that far.
        after  = cls.find_xls_filenames("/tmp")
        change = set(after) - set(cls.tmp_file_before)
        file_name ="no file exists"
        if len(change) == 1:
            file_name = change.pop()
        else:
            print "More than one file or no file downloaded"

        print "file_name to be deleted: " + file_name

        if os.path.isfile('/tmp/'+ file_name):
            os.remove('/tmp/'+ file_name)

        cls.driver.quit()

        #quit the ghost window
        cls.display.stop()

    ALL_TESTS = {
        'test_01_login' : {
            'test_class': login_test.LoginTest,
            'test_method' : 'test_login'
        },
        'test_02_new_form': {
            'test_class': new_form_from_scratch_test.NewFormFromScratchTest,
            'test_method' : 'create_new_form_from_scratch'
        },
        'test_03_add_sample_question': {
            'test_class': add_sample_questions_test.AddSampleQuestionsTest,
            'test_method': 'add_questions_test'
        },
        'test_04_preview_form': {
            'test_class': preview_form_test.PreviewFormTest,
            'test_method': 'preview_form'
        },
        'test_05_export_form_to_xls': {
            'test_class': export_form_to_xls_test.ExportFormToXlsTest,
            'test_method': 'export_form_to_xls'
        },
        'test_06_delete_all_forms': {
            'test_class': delete_all_forms_test.DeleteAllFormsTest,
            'test_method': 'delete_all_forms'
        },
        'test_07_import_xls_form': {
            'test_class': import_xls_form_test.ImportXlsFormTest,
            'test_method': 'test_import_xls_form'
        },
        'test_08_deploy_form': {
            'test_class': deploy_imported_form_test.DeployImportedFormTest,
            'test_method': 'deploy_form'
        },
        'test_09_submit_from_enketo': {
            'test_class': enketo_form_submission_test.EnketoFormSubmissionTest,
            'test_method': 'submit_from_enketo'
        },
        'test_10_export_data': {
            'test_class': export_data_to_xls_test.ExportDataToXls,
            'test_method': 'export_data'
        },
        'test_11_delete_form': {
            'test_class': delete_form_test.DeleteFormTest,
            'test_method': 'delete_form'
        },
        'test_12_test_verify_no_forms': {
            'test_class': verify_no_forms_test.VerifyNoFormsTest,
            'test_method': 'test_verify_no_forms'
        },
        'test_13_test_logout': {
            'test_class': logout_test.LogoutTest,
            'test_method': 'test_logout'
        }
    }


    def test_step_00_run_all(self):
        running_config = config.environments[self.ENV_TYPE]
        print "running_config:"
        print running_config

        self.base_url = running_config.get('base_url')
        self.username = running_config.get('username')
        self.password = running_config.get('password')

        for key, current_test in sorted(self.ALL_TESTS.iteritems()) :
            test_case_class= current_test.get('test_class')
            test_case_class.__dict__[current_test.get('test_method')](self)



if __name__ == "__main__":
    flag_without_dashes = 'local'
    suite = unittest.TestSuite()
    if len(sys.argv) > 1:
        flag_without_dashes = sys.argv[1]
    Test_Selenium.ENV_TYPE = flag_without_dashes
    suite.addTest(Test_Selenium("test_step_00_run_all"))
    unittest.TextTestRunner().run(suite)
    # unittest.main()
