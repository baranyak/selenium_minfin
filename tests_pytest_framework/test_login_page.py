__author__ = 'mbaranyak'

import pages
import config
from tests_pytest_framework.BaseClass import BaseClass


class TestLogIn(BaseClass):
    def test_login(self):
        main_page = pages.MainPage(self.driver)
        main_page.click_entrance_button()
        main_page.log_in(config.USERNAME, config.PASSWORD)
        assert main_page.user_bar_presence(), 'fail to login'

    def test_entrance_window(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.click_entrance_button(), 'login page is not displayed'

    def test_invalid_login(self):
        main_page = pages.MainPage(self.driver)
        main_page.click_entrance_button()
        failed_login_page = main_page.log_in(config.FALSE_USERNAME, config.FALSE_PASSWORD)
        assert failed_login_page.login_error_message_presence(), 'login error message is not displayed'

