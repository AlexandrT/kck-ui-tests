import pytest
import logging

from lib.fixtures import expected_data
from helpers.utils import *
from helpers.page import *


logger = logging.getLogger('ui_site')
PATH = f"/{current_locale()}/signin"

class TestAuth:
    """Test signin"""

    def setup_class(cls):
        cls.translator = CustomTranslator()
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_ok(self, selenium, main_url):
        """is ok"""

        selenium.get(f"{main_url}{PATH}")
        signin_page = SigninPage(selenium)

        signin_page.login = expected_data.VALID_CREDS['login']
        signin_page.password = expected_data.VALID_CREDS['password']

        signin_page.click_signin_btn()

        assert signin_page.is_profile_btn_existed() == True

    @pytest.mark.parametrize(
        "credentials", expected_data.INVALID_CREDS
    )
    def test_invalid_creds(self, selenium, main_url, credentials):
        """with invalid credentials"""

        selenium.get(f"{main_url}{PATH}")
        signin_page = SigninPage(selenium)

        signin_page.login = credentials['login']
        signin_page.password = credentials['password']

        signin_page.click_signin_btn()

        assert signin_page.is_profile_btn_existed() == False
        assert signin_page.get_login_error() == self.translator.get_translation(f"kck.signin_form.login_error")
